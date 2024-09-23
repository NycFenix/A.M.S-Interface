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
        self.Sh = Sh    # Specific Heat (cal/g*°C) #TODO: Mudar para J/g*°C
        self.Ct = Ct    # Thermal Conductivity (W/m*°C) TODO: Mudar para W/mm*°C
        self.De = De    # Density   (g/cm^3) TODO: Mudar para g/mm^3
        self.Vi = Vi    # Viscosity
        self.Em = Em    # Emissivity
        self.CLFus = CLFus  # Latent Heat of Fusion (J/g)
        self.n = n  # Transfer Mode Eficiency  TODO: Deixar mudança de modo de soldagem com valor default no radiobutton
        

        # Calculated Parameters
        
        self.Pot = self.I*self.V  # Potency (Watts)
        self.h, self.w = self.getBeadGeometry() # Height and Width of the weld bead
        self.Pe = self.getPenetration()  # Penetration Depth
        self.PRratio = self.Pe/(self.w/2)  # Penetration/ radius Ratio
        self.theta1 = 33.18*(self.PRratio**2) - 123.74*self.PRratio + 90.54 # Angulo em graus
        self.theta2 = self.theta1 * 3.1416/180                              # Angulo em radianos
        
        
        
        

        
        self.t_halfway = (self.w/2)/self.Ts     # Time to run 1/2 times the width of the weld bead

        self.Et = (self.n * self.I * self.V/self.Ts) * (self.w/2)  # Total Energy Given

        self.Vf = self.__getVolume()  # Total Volume of the weld bead
        self.As1, self.As2, self.As3, self.As4 = self.__getSurfaces() # Surface Areeas of the weld bead


        # Delta T cálculo (se estiver um número grande (ou negativo), tá errado)

        DeltaTa = ((self.I * self.V)/self.Ts) * self.w/2
        DeltaTb = (((self.h + self.Pe)/2) + (self.h/2))/2
        DeltaT_num = DeltaTa - (self.De * (self.w/2 * 3.1416 * DeltaTb) * self.Sh * (self.Mp - Tamb))
        DeltaT_den = self.Sh * self.De * DeltaTb
        self.DelT = DeltaT_num/DeltaT_den
        self.DelT2 = self.DelT/3
        self.DelT3 = self.DelT/16

        # Energy Calculations
        self.Efus = self.De * self.Vf * self.Sh * (self.Mp - 25) # Energia de fusão necessária para fundir a peça
        # Assume=se que a temperatura ambiente é 25°C
        self.Potcond1 = self.Ct * (self.Mp + self.DelT2 - Tamb) * (self.As1/((self.Pe + self.h)/2))
        self.Potcond2 = self.Ct * 20 * (self.As2/(self.Pe/2))
        self.Prad = self.Em * sigma * ((self.Mp + self.DelT3)**4) * (self.As3 + self.As4)
        self.Potconv = Convt * ((self.Mp + self.DelT2 - Tamb) + 273) * (self.As3 + self.As4) # Potência de Energia Liberada por Convecção
        self.Ecl = self.De * self.Vf * self.CLFus # Energia Liberada pela formação de cristais
        
        self.Tsolid = self.getTsolid()
    def getTsolid(self):

        Numerator = (self.Et + self.Ecl - self.Efus
        - self.t_halfway * (self.Potcond1 + self.Potcond2 + self.Prad + self.Potconv))

        Denominator = self.Potcond1 + self.Potcond2 + self.Prad + self.Potconv

        t_sol = Numerator/Denominator

        return t_sol

    def getBeadGeometry(self):
        '''Calculates the height and width of the weld bead'''      
        r = self.D/2

       
        #E_d = Pot/self.Ts not used

        # Semicircular bead height
        Hi = ((2*(self.Ws/self.Ts) * (r) **2)**0.5)       # Hi = Ai #TODO: elevar ao quadrado so o raio ou a expressão toda?
        # Semicircular bead width
        Wi = 2*Hi                            # Wi = Li

        # To be changed in the future
        # Ce2 = Sh * 4.186        # j / g* °C
        # Ct2 = Ct * 1/1000       # W / mm °K
        # Vi2 = Vi * 1000 / 1000  # g / mm*s  
        # De2 = De * (1/1000)     # g / mm^3
        
       
        #////////
        #Pot1 = 0.45*Pot  Only used if DeltaA is needed
        #Cpr = 0.00048     Only used if DeltaA is needed
        #//////////
        #DelA = Cpr*(Pot1/self.Ts) * ((2)**0.5) * Hi* (t_so) **0.5
        
        #print("DelA: ", DelA)
        #print("Hi: ", Hi)  // +- correct
        #print("Wi: ", Wi)  // +- correct
        #h = Hi - DelA
        #w = 2*Hi + (11.985 * (DelA/Hi)**2 + 14.4 * (DelA/Hi)) * DelA

        return Hi, Wi

    def __getSurfaces(self):
        '''Calculates multiple different surfaces of the weld bead'''

        # Área 1 (Superfície líquida em contato com o substrato sólido)
        a1 = self.w/2
        b1 = 3*self.w/4
        c1 = self.Pe
        
        As1num = ((a1*b1)**1.6075 + (b1*c1)**1.6075 + (a1*c1)**1.6075)/3
        As1 = (2*np.pi) * (As1num)**(1/1.6075) 

        # Área 2 (Superfície aproximada que perde calor para o próprio cordão)
        a2 = self.w/(2**0.5)
        b2 = self.w/2

        As2 = np.pi * a2 * b2

        # Área 3 (Área em contato com o ar aproximada para uma fatia de cilindro)
        
        As3 = self.theta2*(self.w**2)/4
        
        # Área 4 (Superfície da poça inicial)

        As4 = np.pi * (self.w**2)/8

        return As1, As2, As3, As4

    def __getVolume(self):
        '''Calculates total volume of the weld bead'''

        # Volume 1 (Volume da calota fundida no substrato)
        c1 = self.w/2*self.theta1
        
        v1 = (np.pi/3) * self.Pe**2 *(3*c1 - self.Pe) 

        # Volume 2 (Volume da calota ao se movimentar uma distância w/2 com a tocha)

        v2 = (self.w**2)/2 * self.Pe * np.pi
        
        # Volume 3 (Volume fundido depositado na chapa ao percorrer metade da largura com a tocha)

        v3 = np.pi/16 * (self.w**2)

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

        print("a: ", a)
        print("b: ", b)
        print("Pe: ", Pe)
        return Pe

#Usar 0.7 segundos para o tempo de soldagem por enquanto
def getT_Sol(Sh, D, Ts, I, V, De, Pe, Mp, Ct, Ws): #TODO: Acertar a formula a respeito do numerador (valor negativo)
    '''Calculates the solidification time of the weld bead.
    /////////////////////////////////////////////////
    PARAMS:
    Sh: Specific Heat
    D: Diameter
    Ts: Travel Speed
    I: Current
    V: Tension
    De: Density
    Pe: Penetration Depth
    Mp: Melting Point
    Ct: Thermal Conductivity
    Ws: Wire Feet Speed
    '''
    r = D/2
    Pot = I*V

    Hi = ((2*Ws/Ts) * (r **2) ** 0.5)
    Wi = 2*Hi

    Ct2 = Ct * 1/1000 # W/mm^2 * °K Unit

    # Thermal Conveccion Coeficient
    Convt = 100

    Convt2 = Convt/1000000 # W / mm^2 * °K

    Ce2 = Sh * (4.184 * 0.001) / (1*274)       # KJ / g * °K
    De2 = De* (1/1000)      # g/mm

    Mp += 273 # Converting to Kelvin
    Tam2 = 20 + 273

    T_ins = 0.5*Wi/Ts   # Time to run 1/2 times the width. Instant time

    sigma = 5.67e-14    # W/ mm^2 * K^4
    emiss = 0.7

    # # Break down the numerator variable into other little readable variables
    # Numerator_1 = (0.45 * I * V / Ts) * Wi / 2
    # Numerator_2 = De2 * ((np.pi * (Wi / 4) * (Hi ** 2) / 2 + np.pi * (4 / 6) * (Hi ** 3)) + (np.pi * (4 / 6) * (Pe ** 3) + np.pi * (Wi / 4) * (Pe ** 2) / 2)) * Ce2 * Mp
    # Numerator_3 = Ct2 * 1973 * Wi + Convt2 * (2 * np.pi * (Hi ** 2) + (Wi / 4) * np.pi * Hi) * 1973 + emiss * sigma * (1973 ** 4) * (2 * np.pi * (Hi ** 2) + (Wi / 4) * np.pi * Hi)
    # Numerator_alpha = Numerator_1 - Numerator_2 - Numerator_3

    NumeratorA = (0.45*I*V/Ts) * Wi/2
    NumeratorB = De2 * ((np.pi * (Wi/4) * (Hi**2)/2 + (np.pi * (4/6) * (Hi**3)))+(np.pi * (4/6) * (Pe**3) + np.pi * (Wi/4) * (Pe**2)/2)) * Ce2 * (Mp)
    NumeratorC = Ct2 * 1973 * Wi + Convt2 * (2*np.pi * (Hi**2) + (Wi/4) * np.pi * Hi) * 1973 + emiss * sigma * ((1973)**4) * (2*np.pi * (Hi**2) + (Wi/4) * np.pi * Hi) *T_ins
    
    Numerator= (
        NumeratorA - 
        NumeratorB - 
        NumeratorC)
    
    Denominator = (Ct2 * (Mp - Tam2) * Wi
                   + Convt2 * (2*np.pi * (Hi**2) + (Wi/4) * np.pi * Hi)
                    * (Mp - Tam2)
                     + emiss * sigma * ((Mp**4) * (2*np.pi*(Hi**2) + (Wi/4) * np.pi * Hi)))

    print("Numerador A: ", NumeratorA)
    print("Numerador B: ", NumeratorB)
    print("Numerador C: ", NumeratorC)
    print("T_ins: ", T_ins)
    print("Numerator: ", Numerator)
    print("Denominator: ", Denominator)
    # print("numerator_alpha: ", Numerator_alpha)
    t_sol = (Numerator/Denominator)

    return t_sol

def getBeadGeometry(self, D, Ws, Ts, I, V, t_so, De, Sh, Vi, Ct = None):
    '''Calculates the height and width of the weld bead
    /////////////////////////////////////////////////
    PARAMS:
    D: Diameter
    Ws: Wire Feet Speed
    Ts: Travel Speed
    I: Current
    V: Tension
    t_so: Solidification Time
    De: Density
    Sh: Specific Heat
    Vi: Viscosity
    Ct: Thermal Conductivity
    '''
    
    r = D/2

    Pot = I*V
    E_d = Pot/Ts

    # Semicircular bead height
    Hi = ((2*(Ws/Ts) * (r) **2)**0.5)       # Hi = Ai #TODO: elevar ao quadrado so o raio ou a expressão toda?
    # Semicircular bead width
    Wi = 2*Hi                            # Wi = Li

    # To be changed in the future
    # Ce2 = Sh * 4.186        # j / g* °C
    # Ct2 = Ct * 1/1000       # W / mm °K
    # Vi2 = Vi * 1000 / 1000  # g / mm*s  
    # De2 = De * (1/1000)     # g / mm^3

    Pot1 = 0.45*Pot 

    Cpr = 0.00048

    DelA = Cpr*(Pot1/Ts) * ((2)**0.5) * Hi* (t_so) **0.5
    
    print("DelA: ", DelA)
    #print("Hi: ", Hi)  // +- correct
    #print("Wi: ", Wi)  // +- correct
    h = Hi - DelA
    w = 2*Hi + (11.985 * (DelA/Hi)**2 + 14.4 * (DelA/Hi)) * DelA

    return h, w

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
