# This module contains Algorithms and functions used in the geometry_prediction tab
import numpy as np
import math


class BeadGeometry:
    def __init__(self, D, Ws, Ts, I, V, Mp, Sh, Ct, De, Vi, Em, CLFus, n, DBCP):
        # Constans
        self.sigma = 5.67e-14  # W/mm^2 * K^4
        Tamb = 25 # C°
        Tamb2 = Tamb + 273 # K
        self.Convt = 100/1000000 # Conversion coefficient (W / mm^2 * °K)
        self.eficiency = 0.88

        #Given Parameters
        self.D = D  # Diameter
        self.Ws = Ws    # Wire Feet Speed
        self.Ts = Ts    # Travel Speed
        self.I = I    # Current (A)
        self.V = V  # Tension (v)
        self.Mp = Mp    # Melting Point (°C)
        self.Sh = Sh    # Specific Heat (cal/g*°C) 
        self.Ct = Ct    # Thermal Conductivity (W/m*°C) 
        self.De = De    # Density   (g/cm^3) 
        self.Vi = Vi    # Viscosity (g/mm*s)
        self.Em = Em    # Emissivity
        self.CLFus = CLFus  # Latent Heat of Fusion (J/g)
        self.n = n  # Transfer Mode Eficiency 
        self.DBCP = DBCP
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
        self.r = self.eficiency * self.I * self.V / (self.Mp2 - 25) # r = penetração considerando a temperatura do ponto de fusão
        self.Desloc =  self.w/25 # Deslocamento da tocha escolhido (muito menor que a largura)
        self.PeMF = self.getPenetration2()  # Penetration Depth
        self.PRratio = self.PeMF/(self.w/2)
        self.theta1 = 33.18*(self.PRratio**2) - 123.74*self.PRratio + 90.54 # Angulo em graus
        self.theta2 = self.theta1 * 3.1416/180 # Angulo em radianos
        self.temFun = self.Desloc/self.Ts # Tempo que a tocha fica depositando
        # Volume and Surfaces
        self.Vf, self.mass = self.__getVolumeandMass()  # Total Volume of the weld bead
        #self.As1, self.As2, self.As3, self.As4 = self.__getSurfaces() # Surface Areas of the weld bead
        
        self.As3I = np.pi * (self.w/2)**2 # Área superfícial na parte superior da poça
        self.As4I = self.w/2 * self.Desloc # Área superficial da zona fundida na parte superior
        self.AsIConv = self.As3I + self.As4I # Área total fundida exposta a conveccção e radiação
        # //////////////////////////////////////////////////
        # Energy Calculations

        self.t_halfway = (self.w/2)/self.Ts     # Time to run 1/2 times the width of the weld bead
        self.Ecl = self.mass* self.CLFus # Energia necessaria para fundir
        self.Tmax1 = (((self.eficiency * self.I * self.V/self.Ts) * self.Desloc) + self.mass * self.Sh2 * Tamb2 + self.Ecl - self.Ct2*self.Temp2 *
                      (self.De2 * self.Sh2 * self.Ts * self.As3I/ (4*self.Ct2)) * self.temFun - self.Convt * self.Temp2 * self.AsIConv * self.temFun -
                      self.Em * self.sigma * (self.Mp2 ** 4) * self.AsIConv * self.temFun) / (self.mass * self.Sh2) # Temperatura máxima no ponto de fusão
        
        
        # Energy Calculations
        self.Comp = self.w/4 # Comprimento do cordão de solda percorrido
        self.tcomp = self.Comp/self.Ts # Tempo para percorrer o comprimento do cordão de solda
        
        self.PotCond, self.PotConv, self.PotRad, self.Efus, self.Et = self.__getHeatLoss()
        self.Et = (self.n * self.I * self.V/self.Ts) * (self.w/2)  # Total Energy Given


    def getT_sol(self):
        # Método 1 - Modelo matemático
        tsol_M1 = ((self.Et + self.Ecl - self.Efus - self.tcomp*(self.PotCond + self.PotRad + self.PotConv))
        / (self.PotCond + self.PotRad + self.PotConv)) # Considera perdas de conducao convecção e radiação e a energia dada pela fonte

        # Método 2 - Modelo matemático 2

        tsol2_sem = ((4/3) * (np.pi * (0.25 * self.PeMF + 0.25*self.r + 0.5*self.h)**3)/ (self.Ct2M * self.Ts / (4*self.De2*self.Sh2F)))**0.5
        # Calculo anterior propõe uma perda de calor mínima por radiação e convecção durante a solidificação
        tsol_M2 = tsol2_sem * 0.95 ** (self.eficiency * self.I * self.V * self.tcomp / self.Efus)

        # /////////////////////////////////////////////////
        # TEMPO DE SOLIDIFICAÇÃO QUANDO O SUBSTRATO ESTÁ QUENTE
        Tsub = 200 # Temperatura do substrato

        ASuperficie = 40000 # Área superficial do substrato usado como teste TODO: deixar dinâmico no futuro

        tempoSimulado = 100 # TODO: deixar como input na interface depois
        incremento = 0
        tempoT = 0
        for i in range(tempoSimulado):
            tempoT += i
            incre1 = tempoT ** (1/tempoT)
            incremento +=  incre1
        
        tsolF2 = (0.3 * tsol_M1 + 0.7 * tsol_M2) # Pesos determinados empiricamente
        tsolFt = tsolF2 + ((tsolF2)*((self.Ct2 * self.Ws) / self.Ts) * (self.w * (self.Ts * tempoSimulado)/ASuperficie)* (incremento) ** 0.5)
        
        return tsolFt
    
    def getBeadGeometry(self):
        '''Calculates the height and width of the weld bead'''
        
        # Semicircular bead height
        Hi = (2*(self.Ws/self.Ts) * (self.Ra **2))**0.5
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

        E_d1 = self.Pot/self.Ts   # J/mm  
        E_d2 = E_d1/1000         # KJ/mm 
        E_d = E_d2 * 0.2388      # Kcal/mm

        Ce2 = self.Sh/1000            # Kcal/g*°C

        # Constant Paremeters

        Cp1 = 0.1
        Cp2 = 0.054423      # All in unit S^4g
        Cp3 = 0.021

        a = (self.Ws/(Cp1 + ((self.Ts-4)**2)**0.5))   # a 
        b = self.Ts**2*(((E_d*Cp2)/(self.DBCP * self.Mp *Ce2))**0.5) #b
        Pe = (a*b)*Cp3      

        return Pe
    
    def __getHeatLoss(self):
        '''Calculates the multiple sources of heat and energy loss from the welding process'''

        Difus = (self.Ct2 / self.De2*self.Sh2) # Difusividade
        Delt2 = self.Tmax1 - self.Mp2 # Diferença de temperatura entre a temperatura máxima e o ponto de fusão

        #Incremento do Delta2 ao percorrer uma distância maior
        Delt3 = Delt2 * (1 + (self.Comp/ (self.Comp + (self.Desloc/self.Comp)**0.5))/2)
        
        A_poca = np.pi * (self.w/2)**2 # Área da poça de fusão
        DeltReal = (A_poca * (1/25) * Delt3 + A_poca * (8/25) * (Delt3/2))/25 # Distribuição do incremento máximo na área da poça
                                            

        # PERDA POR CONDUTIVIDADE
        # constantes de posição
        con1 = 1 # Se o calor foi distribuido do centro do corpo para fora
        con2 = 0.5 # Se o calor foi distribuído de um plano para dentro de um corpo
        con3 = 0.25 # Se o calor foi distribuido de uma lateral do corpo
        con4 = 0.125 # Se o calor foi distribuído de uma quina

        Eixo_trans = 3 # Eixo no que se transmite o calor

        # Ao passar do tempo o ponto intermediário entre duas distancias
        #  muito pequenas, entre duas temperaturas, aumenta sua T°, 
        # pode-se considerar este ponto com aumento de T° intermediário
        # de 1/2*DeltaT°, mais quente que o instante anterior . (Traduzido dos comentários do Jairo)
        
        ## Influencia do acumulo de calor na condução - Constante proposta para trajetoria oscilada
        Acum_oscilado = 6 * Difus / self.Ts * self.h # TODO: não utilizado

        ## Influência do acumulod e calor na condução - constante proposta para trajetoria filetada ou paralela
        Acum_raster = 4 * Difus / self.Ts * self.h

        ConsCond = Eixo_trans * con2/Acum_raster

        Pcond1 = self.Ct2F * (self.Mp2 + (Delt2 / (np.pi * ((self.w/2)**2))) - self.Tamb2) * (2*(np.pi * ((self.w/2)**2)) / (self.h + self.PeMF)) * ConsCond
        
        # PERDA POR CONVECÇÃO
        
        Pconv = self.Convt * (self.Mp2 + (Delt3 / (np.pi * ((self.w/2) ** 2))) - self.Tamb2) * self.AsIConv 

        # PERDA POR RADIAÇÃO

        Prad = self.Em * self.sigma * (self.Mp + (Delt3 / (np.pi *((self.w/2) ** 2)))) ** 4 * self.AsIConv

        Q = 4 * np.pi * Difus * self.r * DeltReal * math.e**(self.r**2 / (4* Difus * self.tcomp)) / self.tcomp # TODO: não utilizado

        Et = (self.eficiency * self.I * self.V /self.Ts) * self.Comp
        Efus = self.mass * self.Sh2 * (self.Mp2 - self.Tamb2)

        #Result = Et - Efus # TODO: não usado?

        return Pcond1, Pconv, Prad, Efus, Et
        # return Potencial de condução, 
        # potencial de convecção, 
        # potencial de radiação,
        # energia de fusão,
        # energia total

    def getPenetration2(self): #Modelo matemático usando fórmulas de termodinâmica
        
        #Penetração 2.1: relação da penetração semiesférica radial a semielíptica - Distribuição igual de ÁREAS 
        Penetr1 = self.r**2 / (self.w/2)
        #Penetração 2.2: relação da penetração semiesférica radial a semielíptica - Distribuição igual de VOLUMES
        Penetr2 = self.r**3 / (self.w/2)**2
        #Penetração 2.3: Relação da penetração considerando relação entre corrente e Tensão
        Penetr3 = self.r*self.I/ (12 * self.V) #NOTA: 12 é a constante para o aço

        #Média de todas as penetrações com os seus determinados pesos
        Pe = self.getPenetration1()
        print("Penetr1: ", Penetr1)
        print("Penetr2: ", Penetr2)
        print("Penetr3: ", Penetr3)
        print("Pe: ", Pe)
        PeFinal = (0.5 * Penetr1 + 0.08*Penetr2 + 0.12*Penetr3 + 0.3*Pe) # Pesos determinados empiricamente
        return PeFinal  
  
