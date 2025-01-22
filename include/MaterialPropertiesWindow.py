import pandas as pd
from PySide6.QtWidgets import QWidget
from PySide6.QtWidgets import QLabel
from PySide6.QtWidgets import QFileDialog
from PySide6.QtWidgets import QInputDialog
from PySide6.QtGui import QPixmap
from PySide6.QtUiTools import QUiLoader
from PySide6.QtCore import QFile
class MaterialPropertiesForm(QWidget):


    def __init__(self) -> None:
        super(MaterialPropertiesForm, self).__init__()
        ui_file = QFile("include/ui/MaterialPropertiesWindow.ui")
        ui_file.open(QFile.ReadOnly)
        loader = QUiLoader()
        self.ui = loader.load(ui_file, self)
        ui_file.close()
        
    def closeEvent(self, event):
        self.hide()
        event.ignore()
        

arquivo = "Material Properties.xlsx"