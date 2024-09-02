# This module contains Algorithms and functions used in the geometry_prediction tab
import numpy as np
import math

def getPenetration(V, I, Ws, Ts, Mp, Sh): #Acertar fórmula: valores muito baixos de penetração
    '''Calculates the penetration depth of the weld bead
    /////////////////////////////////////////////////
    PARAMS:
    V: Tension
    I: Current
    Ws: Wire Feet Speed
    Ts: Travel Speed
    Mp: Melting Point
    Sh: Specific Heat
    '''

    
    # Ws  = Ws * 1000/60
    # Ts = Ts * 1000 / 60

    Pot = I / V  # Watt
    E_d1 = Pot/Ts   # J/mm  
    E_d2 = E_d1/1000         # KJ/mm 
    E_d = E_d2 * 0.2388      # Kcal/mm

    Ce2 = Sh/1000            # Kcal/g*°C

    # Constant Paremeters

    Cp1 = 0.1
    Cp2 = 0.054423      # All in unit S^4g
    Cp3 = 0.021

    DBCP = 15  #distancia da tocha ao á peça (Distancia Bico de Contato Peça) em mm

    a = (Ws/(Cp1 + ((Ts-4)**2)**0.5))   # a 
    b = Ts**2*(((E_d*Cp2)/(DBCP * Mp *Ce2))**0.5)
    Pe = (a*b)*Cp3

    print("a: ", a)
    print("b: ", b)
    print("Pe: ", Pe)
    return Pe

#Usar 0.7 segundos para o tempo de soldagem por enquanto
def getT_Sol(Sh, D, Ts, I, V, De, Pe, Mp, Ct, Ws): #TODO: Acertar a formula a respeito do numerador (valor negativo)
    '''Calculates the solidification time of the weld bead.
    /////////////////////////////////////////////////]
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

def getBeadGeometry(D, Ws, Ts, I, V, t_so, De, Sh, Vi, Ct = None):
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