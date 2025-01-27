
from include import BeadGeometry
from PySide6.QtWidgets import QMainWindow
from PySide6.QtWidgets import QLabel
from PySide6.QtWidgets import QFileDialog, QApplication
from PySide6.QtWidgets import QInputDialog
from PySide6.QtGui import QPixmap
import os
from include.AMS_ui import Ui_AMS_Interface
from PySide6.QtCore import QFile
from PySide6.QtUiTools import QUiLoader
from include import MaterialPropertiesWindow
class AMSInterface(QMainWindow):
    '''Class that contains all methods and atributes of the interface hat do not belong to the UI file
    
    Parameters:
    ----------------
    QMainWindow: Base class for all windows in PySide6. Has to be inherited to create a window in PySide6.'''


    def __init__(self) -> None:

        super(AMSInterface, self).__init__()

        ui_file = QFile("include/ui/AMS_ui.ui")
        ui_file.open(QFile.ReadOnly)
        loader = QUiLoader()
        self.ui = loader.load(ui_file, self)
        ui_file.close()
        self.setCentralWidget(self.ui)

        self.MaterialPropertiesForm = MaterialPropertiesWindow.MaterialPropertiesForm()

        # self.ui = Ui_AMS_Interface()
        


        # HERE END THE LOADING WINDOW PART







        # Defining global variable as to not have to repeat it every time
        global ui
        ui = self.ui

        
        title = "AMS Interface"
        description = "Interface for Adictivie Manufacturing Projects developed by LNTSOLD team" # TODO: Figure out where to put this
        version = "0.1"                                                                          # TODO: Same as above
        self.setWindowTitle(title)


         # /////////////////////////////////////////////

        # AUTOMATIONS

        ui.cmt.setChecked(True) # Default Transfer Mode
        n_eficiency = self.EficiencyButton()
        ui.ws_input1.textEdited.connect(lambda: ui.ws_input2.setText(self.SpeedMeasureConverter(ui.ws_input1.text(), 1)))
        ui.ws_input2.textEdited.connect(lambda: ui.ws_input1.setText(self.SpeedMeasureConverter(ui.ws_input2.text(), -1)))

        ui.ts_input1.textEdited.connect(lambda: ui.ts_input2.setText(self.SpeedMeasureConverter(ui.ts_input1.text(), 1)))
        ui.ts_input2.textEdited.connect(lambda: ui.ts_input1.setText(self.SpeedMeasureConverter(ui.ts_input2.text(), -1)))


        ui.destroyed.connect(QApplication.quit)
        # /////////////////////////////////////////////


    

        # BUTTONS

        ui.calculate_button.clicked.connect(lambda: self.GeometricPredictionCallback(Ws=ui.ws_input1.text(), Ts=ui.ts_input1.text(), V=ui.v_input.text(), 
                                                                                     I=ui.I.text(), Mp=ui.melting_point.text(), Sh=ui.specific_heat.text(), 
                                                                                     Vi=ui.viscosity.text(), De=ui.density.text(), Ct=ui.thermal_conductivity.text(), 
                                                                    D=ui.diameter.text(), Em=ui.emissivity.text(), CLFus=ui.EnthalpyFusion.text(), 
                                                                    n=n_eficiency, DBCP=ui.DBCP.text()))

        ui.Analyzebttn.clicked.connect(lambda: self.LoadImg(ui.AnalyzedImg))             
      
        ui.MaterialsButton.clicked.connect(lambda: self.MaterialPropertiesCallback())
        # Default Parameters: Common Steel

        mp_default = 1420   # Melting Point
        sh_default = 0.11   # Specific Heat
        vi_default = 0.003  # Viscosity
        de_default = 7.89   # Density
        ct_default = 71.5   # Thermal Conductivity
        em_default = 0.7   # Emissivity
        ef_default = 25     # Enthalpy Fusion
        DBCP_default = 15
        
        ui.melting_point.setText(str(mp_default))
        ui.specific_heat.setText(str(sh_default))
        ui.viscosity.setText(str(vi_default))
        ui.density.setText(str(de_default))
        ui.thermal_conductivity.setText(str(ct_default))
        ui.emissivity.setText(str(em_default))
        ui.EnthalpyFusion.setText(str(ef_default))
        ui.DBCP.setText(str(DBCP_default))

        # Default Parameters: valores usados no codigo no MatLab 

        ui.ws_input2.setText("5")
        ui.ts_input1.setText("10.83")
        ui.v_input.setText("20.1")
        ui.I.setText("129")
        ui.diameter.setText("1.2")

        # ///////////////////////////////////////////////////

    def GeometricPredictionCallback(self, D, Ws, Ts, I, V, Mp, Sh, Ct, De, Vi, Em, CLFus, n, DBCP) -> None:
            

            # Como a classe de cálculo só aceita em mm/s, é necessário converter para mm/s quando não for essa a unidade usada no input
            try :
                Ws = float(Ws)
            except ValueError:
                Ws = self.SpeedMeasureConverter(ui.ws_input2.text(), -1)
                ui.ws_input1.setText(Ws)
                Ws = float(Ws)
            
            try:
                Ts = float(Ts)
            except ValueError:
                Ts = self.SpeedMeasureConverter(ui.ts_input2.text(), -1)
                ui.ts_input1.setText(Ts)
                Ts = float(Ts)

            # Converterndo tudo pra float
            # TODO: ta muito feio, fazer de forma mais elegante
            V = float(V)
            I = float(I)
            Mp = float(Mp)
            Sh = float(Sh)
            Ct = float(Ct)
            De = float(De)
            Vi = float(Vi)
            Em = float(Em)
            CLFus = float(CLFus)
            n = float(n)
            DBCP = float(DBCP)
            D = float(D)


            Geometry = BeadGeometry.BeadGeometry(D, Ws, Ts, I, V, Mp, Sh, Ct, De, Vi, Em, CLFus, n, DBCP) #Initiate GeomtryObject
            height, width = Geometry.h, Geometry.w #Get Bead Geometry
            penetration = Geometry.PeMF #Get Penetration
            t_solid = Geometry.getTSolid2() #Get Solidification Time of Bead
            TMax = Geometry.Tmax1 #Get Maximum Temperature
            TMax -= 273.15 #Convert to Celsius

            #t_solid = BeadGeometry.getT_Sol(Sh, D, Ts, I, V, De, penetration, Mp, Ct, Ws)
            #t_solid = 1 #Valor temporário
            
            ui.penetration.setText(str(round(penetration, 3)))
            ui.t_solid.setText(str(round(t_solid,3)))
            ui.height.setText(str(round(height,3)))
            ui.width.setText(str(round(width,3)))
            ui.Tmax.setText(str(round(TMax,3)))

    def SpeedMeasureConverter(self, speed = str,flag = int) -> str:
        #This method converts mm/s into m/min and vice-versa
        # If flag = 1, mm/s -> m/min
        # if its -1, m/min -> mm/s
        
        try:
            speed = float(speed)
            new_speed  = speed * ((60 / 1000) ** flag)
            return str(round(new_speed, 3))
        except ValueError: # If nothing is written or input is invalid, does not convert
            return ""

    def DeltaECallback(self, deltaE = str):
        try:
            deltaE = float(deltaE)
            deltaE = BeadGeometry.getDeltaE(deltaE)
            return str(round(deltaE, 3))
        except ValueError:
            return ""
        

    def EficiencyButton(self):
        if ui.cmt.isChecked():
            return 0.89
        elif ui.mix.isChecked():
            return 0.84
        elif ui.pulsado.isChecked():
            return 0.81

    def LoadImg(self, receiverImg = QLabel) -> None:
        file_filter = "Image Files (*.png *.jpg *.bmp)"
        imgPath, _ = QFileDialog.getOpenFileName(
            parent = self,
            caption = "Select Analyzed Image",
            dir = os.getcwd(),
            filter = file_filter,
            selectedFilter=file_filter
        )
        
        image = QPixmap(imgPath)
        receiverImg.setPixmap(image)
        receiverImg.setScaledContents(True)
        receiverImg.resize(400, 200)
        print("Button Clicked")

    def MaterialPropertiesCallback(self) -> None:
        
        self.MaterialPropertiesForm.show()
        

    def closeEvent(self, event):
        QApplication.quit()
        event.accept()
