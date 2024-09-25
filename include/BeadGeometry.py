# This module contains Algorithms and functions used in the geometry_prediction tab
import numpy as np
import math



class BeadGeometry:
    def __init__(self, D, Ws, Ts, I, V, Mp, Sh, Ct, De, Vi, Em, CLFus, n):
        # Constans
        sigma = 5.67e-14  # W/mm^2 * K^4
        Tamb = 25 # C°
        Convt = 100/1000000 # Conversion coefficient (W / mm^2 * °K)


        #Given Parameters
        self.D = D  # Diameter
        self.Ws = Ws    # Wire Feet Speed
        self.Ts = Ts    # Travel Speed
        self.I = I    # Current (A)
        self.V = V  # Tension (v)
        self.Mp = Mp    # Melting Point (°C)
        self.Sh = Sh    # Specific Heat (cal/g*°C) #TODO: Converter para J/g*°C
        self.Ct = Ct    # Thermal Conductivity (W/m*°C) TODO: Converter para W/mm*°C
        self.De = De    # Density   (g/cm^3) TODO: Converter para g/mm^3
        self.Vi = Vi    # Viscosity (g/mm*s)
        self.Em = Em    # Emissivity
        self.CLFus = CLFus  # Latent Heat of Fusion (J/g)
        self.n = n  # Transfer Mode Eficiency  TODO: Deixar mudança de modo de soldagem com valor default no radiobutton
        

        # Converting to other units

        self.Mp2 = self.Mp + 273 # (°K)
        self.Tamb2 = Tamb + 273 # (°K)

        self.Sh2 = self.Sh * 4.184 # J/g*°C
        self.De2 = self.De / 1000 # g/mm^3
        self.Ct2 = self.Ct / 1000 # W/mm*°C

        # Calculated Parameters
        
        self.Pot = self.I*self.V  # Potency (Watts)
        self.h, self.w = self.getBeadGeometry() # Height and Width of the weld bead
        self.Pe = self.getPenetration()  # Penetration Depth
        self.PRratio = self.Pe/(self.w/2)
        self.theta1 = 33.18*(self.PRratio**2) - 123.74*self.PRratio + 90.54 # Angulo em graus
        self.theta2 = self.theta1 * 3.1416/180                              # Angulo em radianos
        self.Vf = self.__getVolume()  # Total Volume of the weld bead
        self.As1, self.As2, self.As3, self.As4 = self.__getSurfaces() # Surface Areas of the weld bead

        
        self.t_halfway = (self.w/2)/self.Ts     # Time to run 1/2 times the width of the weld bead

        self.Et = (self.n * self.I * self.V/self.Ts) * (self.w/2)  # Total Energy Given

        # Delta T cálculo (se estiver um número grande (ou negativo), tá errado)

        DeltaTa = ((self.I * self.V)/self.Ts) * self.w/2
        DeltaTb = self.Vf
        DeltaT_num = DeltaTa - (self.De2 * (self.w/2 * 3.1416 * DeltaTb) * self.Sh2 * (self.Mp - Tamb))
        print("DeltaNumerador ", DeltaT_num)
       
        DeltaT_den = self.Sh2 * self.De2 * DeltaTb
        print("DeltaDenominador ", DeltaT_den)
        self.DelT = DeltaT_num/DeltaT_den
        print("DeltaTa: ", DeltaTa)
        print("DeltaTb: ", DeltaTb)        

        # Energy Calculations
        self.Efus = self.De2 * self.Vf * self.Sh * (self.Mp - Tamb) # Energia de fusão necessária para fundir a peça
        self.Potcond1 = self.Ct2 * (self.Mp + self.DelT - Tamb) * (self.As1/((self.Pe + self.h)/2))
        print("Delta T: ", self.DelT)
        self.Potcond2 = self.Ct2 * 20 * (self.As2/(self.Pe/2))
        self.Prad = self.Em * sigma * ((self.Mp + self.DelT)**4) * (self.As3 + self.As4)
        self.Potconv = Convt * ((self.Mp + self.DelT - Tamb) + 273) * (self.As3 + self.As4) # Potência de Energia Liberada por Convecção
        self.Ecl = self.De2 * self.Vf * self.CLFus # Energia Liberada pela formação de cristais
        
        self.Tsolid = self.getTsolid()

        
    def getTsolid(self):

        Numerator = (self.Et + self.Ecl - self.Efus
        - self.t_halfway * (self.Potcond1 + self.Potcond2 + self.Prad + self.Potconv))

        Denominator = self.Potcond1 + self.Potcond2 + self.Prad + self.Potconv

        t_sol = Numerator/Denominator
        
        # print("ENERGIAS")
        # print("/////////////////////////////////")
        
        # print("Energia Total necessária: ", self.Et)
        # print("Energia de Fusão: ", self.Efus)
        # print("Densidade: ", self.De2)
        # print("Volume: ", self.Vf)
        # print("Calor Específico: ", self.Sh)
        # print("Temperatura", (self.Mp - 25))
        # print("Energia Liberada pela formação de cristais: ", self.Ecl)
        # print("Potência de Condução 1: ", self.Potcond1)
        # print("Potência de Condução 2: ", self.Potcond2)
        # print("Potência de Radiação: ", self.Prad)
        # print("Potência de Convecção: ", self.Potconv)
        # print("numerador: ", Numerator)
        # print("/////////////////////////////////")
        # print("denominador: ", Denominator)
        # print("Tempo de Solidificação: ", t_sol)


        
        return t_sol

    def getBeadGeometry(self):
        '''Calculates the height and width of the weld bead'''

        r = self.D/2
        
        # Semicircular bead height
        Hi = (2*(self.Ws/self.Ts) * (r **2))**0.5
        Wi = 2*Hi                 
        print("Hi: ", Hi)
        print("Wi: ", Wi)
        print("--------------")
        return Hi, Wi

    def __getSurfaces(self):
        '''Calculates multiple different surfaces of the weld bead'''

        # Área 1 (Superfície líquida em contato com o substrato sólido)
        
        As1num = (((self.w**2) * 3/8)**1.6075) + ((self.w *self.Pe/2)**1.6075) + ((self.Pe * self.w * 3/4)**1.6075)
        As1  = 2*np.pi*(As1num/3)**(1/1.6075) 

        # Área 2 (Superfície aproximada que perde calor para o próprio cordão)
        As2 = (np.pi * (self.w**2))/(4 * math.sqrt(2))

        # Área 3 (Área em contato com o ar aproximada para uma fatia de cilindro)
        
        As3 = self.theta2*(self.w**2)/4
        
        # Área 4 (Superfície da poça inicial)

        As4 = (np.pi * (self.w**2)/8) + (self.w**2/4)

        return As1, As2, As3, As4

    def __getVolume(self):
        '''Calculates total volume of the weld bead'''

        # Volume 1 (Volume da calota fundida no substrato)
        c = self.w/2*math.cos(self.theta2)
        
        v1 = (np.pi/3) * self.Pe**2 *(3*c - self.Pe) 

        # Volume 2 (Volume da calota ao se movimentar uma distância w/2 com a tocha)

        v2 = (self.w**2)/2 * self.Pe * np.pi
        
        # Volume 3 (Volume fundido depositado na chapa ao percorrer metade da largura com a tocha)

        v3 = np.pi/16 * (self.w**3)

        print("Volume 1: ", v1)
        print("Volume 2: ", v2)
        print("Volume 3: ", v3)
        return v1 + v2 + v3
    
    def getPenetration(self): #Acertar fórmula: valores muito baixos de penetração
        '''Calculates the penetration depth of the weld bead'''

        
        # Ws  = Ws * 1000/60
        # Ts = Ts * 1000 / 60

        
        E_d1 = self.Pot/self.Ts   # J/mm  
        E_d2 = E_d1/1000         # KJ/mm 
        E_d = E_d2 * 0.2388      # Kcal/mm

        Ce2 = self.Sh/1000            # Kcal/g*°C

        # Constant Paremeters

        Cp1 = 0.1
        Cp2 = 0.054423      # All in unit S^4g
        Cp3 = 0.021

        DBCP = 15  #distancia da tocha ao á peça (Distancia Bico de Contato Peça) em mm

        a = (self.Ws/(Cp1 + ((self.Ts-4)**2)**0.5))   # a 
        b = self.Ts**2*(((E_d*Cp2)/(DBCP * self.Mp *Ce2))**0.5) #b
        Pe = (a*b)*Cp3      

        # print("a: ", a)
        # print("b: ", b)
        # print("Pe: ", Pe)
        return Pe

#Usar 0.7 segundos para o tempo de soldagem por enquanto

def getDeltaE(I, V, Ts, den, Ws, Sh, Mp, D, t = 1):
    '''Calculates the energy consumed in the welding process
    /////////////////////////////////////////////////
    PARAMS:
    I: Current
    V: Tension
    Ts: Travel Speed
    den: Density
    Ws: Wire Feet Speed
    Sh: Specific Heat
    Mp: Melting Point
    D: Diameter
    t: Time'''
    wire_area = np.pi * (D/2)**2
    DeltaE = ((I*V/Ts) * t) - (Sh * Mp * (den * (wire_area*Ws*t)))
    return DeltaE
