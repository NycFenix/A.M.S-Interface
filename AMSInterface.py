from lib.ui import Ui_AMS_Interface
from include import BeadGeometry
from PySide6.QtWidgets import QMainWindow
from PySide6.QtWidgets import QLabel
from PySide6.QtWidgets import QFileDialog
from PySide6.QtWidgets import QInputDialog
from PySide6.QtGui import QPixmap
import os
class AMSInterface(QMainWindow):
    '''Class that contains all methods and atributes of the interface hat do not belong to the UI file
    
    Parameters:
    ----------------
    QMainWindow: Base class for all windows in PySide6. Has to be inherited to create a window in PySide6.'''


    def __init__(self) -> None:

        super(AMSInterface, self).__init__()

        self.ui = Ui_AMS_Interface()
        self.ui.setupUi(self)

        # Defining global variable as to not have to repeat it every time
        global ui
        ui = self.ui

        
        title = "AMS Interface"
        description = "Interface for Adictivie Manufacturing Projects developed by LNTSOLD team" # TODO: Figure out where to put this
        version = "0.1"                                                                          # TODO: Same as above
        self.setWindowTitle(title)


        # BUTTONS

        ui.calculate_button.clicked.connect(lambda: self.GeometricPredictionCallback(float(ui.ws_input1.text()), float(ui.ts_input1.text()), float(ui.v_input.text()), 
                                                                                     float(ui.I.text()), float(ui.melting_point.text()), float(ui.specific_heat.text()), 
                                                                                     float(ui.viscosity.text()), float(ui.density.text()), float(ui.thermal_conductivity.text()), 
                                                                    float(ui.diameter.text()), float(ui.emissivity.text()), float(ui.EnthalpyFusion.text()), n_eficiency))
        

        ui.Analyzebttn.clicked.connect(lambda: self.LoadImg(ui.AnalyzedImg))             
      
        

        # /////////////////////////////////////////////

        # AUTOMATIONS
        n_eficiency = self.EficiencyButton()
        ui.ws_input1.editingFinished.connect(lambda: ui.ws_input2.setText(self.SpeedMeasureConverter(ui.ws_input1.text(), 1)))
        ui.ws_input2.editingFinished.connect(lambda: ui.ws_input1.setText(self.SpeedMeasureConverter(ui.ws_input2.text(), -1)))

        ui.ts_input1.editingFinished.connect(lambda: ui.ts_input2.setText(self.SpeedMeasureConverter(ui.ts_input1.text(), 1)))
        ui.ts_input2.editingFinished.connect(lambda: ui.ts_input1.setText(self.SpeedMeasureConverter(ui.ts_input2.text(), -1)))

        # /////////////////////////////////////////////



    




        # Default Parameters: Common Steel

        mp_default = 1450   # Melting Point
        sh_default = 0.11   # Specific Heat
        vi_default = 0.003  # Viscosity
        de_default = 7.89   # Density
        ct_default = 71.5   # Thermal Conductivity
        em_default = 0.75   # Emissivity

        ui.melting_point.setText(str(mp_default))
        ui.specific_heat.setText(str(sh_default))
        ui.viscosity.setText(str(vi_default))
        ui.density.setText(str(de_default))
        ui.thermal_conductivity.setText(str(ct_default))
        ui.emissivity.setText(str(em_default))

        # Default Parameters: Análise de dados.xlsx (linha 1)

        ui.ws_input2.setText("3")
        ui.ts_input1.setText("8.33")
        ui.v_input.setText("17.1")
        ui.I.setText("83")
        ui.diameter.setText("1.2")

        # ///////////////////////////////////////////////////



        self.show()

    def GeometricPredictionCallback(self, D, Ws, Ts, I, V, Mp, Sh, Ct, De, Vi, Em, CLFus, n) -> None:
            Geometry = BeadGeometry.BeadGeometry(D, Ws, Ts, I, V, Mp, Sh, Ct, De, Vi, Em, CLFus, n) #Initiate GeomtryObject
            height, width = Geometry.getBeadGeometry() #Get Bead Geometry
            penetration = BeadGeometry.BeadGeometry.getPenetration() #Get Penetration
            t_solid = BeadGeometry.BeadGeometry.getTsolid() #Get Solidification Time of Bead

            

            #t_solid = BeadGeometry.getT_Sol(Sh, D, Ts, I, V, De, penetration, Mp, Ct, Ws)
            #t_solid = 1 #Valor temporário
            
            ui.penetration.setText(str(round(penetration, 3)))
            ui.t_solid.setText(str(round(t_solid,3)))
            ui.height.setText(str(round(height,3)))
            ui.width.setText(str(round(width,3)))


    def SpeedMeasureConverter(self, speed = str,flag = int):
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

