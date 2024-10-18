# This module contains Algorithms and functions used in the geometry_prediction tab
import numpy as np
import math



class BeadGeometry:
    def __init__(self, D, Ws, Ts, I, V, Mp, Sh, Ct, De, Vi, Em, CLFus, n):
        # Constans
        sigma = 5.67e-14  # W/mm^2 * K^4
        Tamb = 25 # C°
        Tamb2 = Tamb + 273 # K
        Convt = 100/1000000 # Conversion coefficient (W / mm^2 * °K)
        self.eficiency = 0.88

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
        self.Sh2F = 1.2*self.Sh2 #usado para valores iguais ou superiores ao ponto de fusão
        self.De2 = self.De / 1000 # g/mm^3
        self.Ct2 = self.Ct / 1000 # W/mm*°K
        self.Ct2F = 0.9*self.Ct2 # W/mm*°K usado para valores iguais ou superiores ao ponto de fusão
        self.Ct2M = (self.Ct2 + self.Ct2F)/2 

        # Calculated Parameters
        
        self.Ra = self.D/2  # Raio do cordão de solda
        self.Pot = self.I*self.V  # Potency (Watts)
        self.Temp2 = self.Mp2 - Tamb2 # Diferença de temperatura entre os pontos de fusao a tamb
        self.h, self.w = self.getBeadGeometry() # Height and Width of the weld bead
        self.Desloc =  self.w/25 # Deslocamento da tocha escolhido (muito menor que a largura)
        self.PeMF = self.getPenetration2()  # Penetration Depth
        self.PRratio = self.Pe/(self.w/2)
        self.theta1 = 33.18*(self.PRratio**2) - 123.74*self.PRratio + 90.54 # Angulo em graus
        self.theta2 = self.theta1 * 3.1416/180 # Angulo em radianos
        self.temFun = self.Desloc/self.Ts # Tempo que a tocha fica depositando
        # Volume and Surfaces
        self.Vf, self.mass = self.__getVolumeandMass()  # Total Volume of the weld bead
        self.As1, self.As2, self.As3, self.As4 = self.__getSurfaces() # Surface Areas of the weld bead
    
        self.As3I = np.pi * (self.w/2)**2 # Área superfícial na parte superior da poça
        self.As4I = self.w/2 * self.Desloc # Área superficial da zona fundida na parte superior
        self.AsIConv = self.As3I + self.As4I # Área total fundida exposta a conveccção e radiação
        # //////////////////////////////////////////////////
        # Energy Calculations

        self.t_halfway = (self.w/2)/self.Ts     # Time to run 1/2 times the width of the weld bead
        
        self.Tmax1 = (((self.eficiency * self.I * self.V/self.Ts) * self.Desloc) + self.mass * self.Sh2 * Tamb2 + self.Ecl - self.Ct2*self.Temp2 *
                      (self.De2 * self.Sh2 * self.Ts * self.As3I/ (4*self.Ct2)) * self.temFun - Convt * self.Temp2 * self.AsIConv * self.temFun -
                      self.Em * sigma * (self.Mp2 ** 4) * self.AsIConv * self.temFun) / (self.mass * self.Sh2) # Temperatura máxima no ponto de fusão
        
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
        self.Potcond1 = self.Ct2F * (self.Mp + self.DelT - Tamb) * (self.As1/((self.Pe + self.h)/2))
        print("Delta T: ", self.DelT)
        self.Potcond2 = self.Ct2 * 20 * (self.As2/(self.Pe/2))
        self.Prad = self.Em * sigma * ((self.Mp + self.DelT)**4) * (self.As3 + self.As4)
        self.Potconv = Convt * ((self.Mp + self.DelT - Tamb) + 273) * (self.As3 + self.As4) # Potência de Energia Liberada por Convecção
        self.Ecl = self.mass* self.CLFus # Energia Liberada pela formação de cristais
        
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
    

    def getTSolid2(self):
        PeFinal = self.getPenetration2()
        r = self.eficiency * self.I * self.V / (self.Mp2 - 25) # r = penetração considerando a temperatura do ponto de fusão


        Comp = self.w/4 # Comprimento do cordão de solda percorrido
        tcomp = Comp/self.Ts # Tempo para percorrer o comprimento do cordão de solda

        tsol2_sem = ((4/3) * (np.pi * (0.25 * PeFinal + 0.25*r + 0.5*self.h)**3)/ (self.Ct2M * self.Ts / (4*self.De2*self.Sh2F)))**0.5
        # Valor de tempo de solidifcação desconsiderando as perdas de radiação e convecção
        # e considerando difusividade "velocidade de transmissão de calor"

        tsol2 = tsol2_sem * (0.95) ** (self.eficiency * self.I * self.V * tcomp / self.Efus)
        #...
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

    def __getVolumeandMass(self):
        '''Calculates total volume of the weld bead'''

        # Volume 1 (Volume da poça fundida - instantânea)
        v1 = (((4/3) * np.pi * (self.w/2)**2)/2) * (self.PeMF / (self.w/2)) 

        # Volume 2 (Volume que funde ao deslocar)

        v2 = ((self.w/2) * self.Desloc * self.PeMF * np.pi)/2
        
        
        print("Volume 1: ", v1)
        print("Volume 2: ", v2)
     
        # Massa      
        massaT = self.De2 * v1 + self.De2 * (np.pi * (self.Ra**2) * self.Ws * (self.Desloc/self.Ts))

        return (v1 + v2), massaT
    
    
    def getPenetration1(self): #Acertar fórmula: valores muito baixos de penetração
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
        #TODO: fazer isso um input na interface

        a = (self.Ws/(Cp1 + ((self.Ts-4)**2)**0.5))   # a 
        b = self.Ts**2*(((E_d*Cp2)/(DBCP * self.Mp *Ce2))**0.5) #b
        Pe = (a*b)*Cp3      

        # print("a: ", a)
        # print("b: ", b)
        # print("Pe: ", Pe)
        return Pe
    

    def getPenetration2(self): #Modelo matemático usando fórmulas de termodinâmica
        r = self.eficiency * self.I * self.V / (self.Mp2 - 25) # r = penetração considerando a temperatura do ponto de fusão

        #Penetração 2.1: relação da penetração semiesférica radial a semielíptica - Distribuição igual de ÁREAS 
        Penetr1 = r**2 / (self.w/2)
        #Penetração 2.2: relação da penetração semiesférica radial a semielíptica - Distribuição igual de VOLUMES
        Penetr2 = r**3 / (self.w/2)**2
        #Penetração 2.3: Relação da penetração considerando relação entre corrente e Tensão
        Penetr3 = r*self.I/ (12 * self.V) #NOTA: 12 é a constante para o aço

        #Média de todas as penetrações com os seus determinados pesos
        Pe = self.getPenetration1()

        PeFinal = (0.5 * Penetr1 + 0.08*Penetr2 + 0.12*Penetr3 + 0.3*Pe) # Pesos determinados empiricamente
        return PeFinal  

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
