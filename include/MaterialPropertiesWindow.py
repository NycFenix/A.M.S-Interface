import pandas as pd
from PySide6.QtWidgets import QWidget
from PySide6.QtWidgets import QLabel
from PySide6.QtWidgets import QFileDialog
from PySide6.QtWidgets import QInputDialog, QTableView, QTableWidget, QTableWidgetItem
from PySide6.QtGui import QPixmap
from PySide6.QtUiTools import QUiLoader
from PySide6.QtCore import QFile

path = "include\Material_Properties.xlsx"
class MaterialPropertiesForm(QWidget):


    def __init__(self) -> None:
        super(MaterialPropertiesForm, self).__init__()
        ui_file = QFile("include/ui/MaterialPropertiesWindow.ui")
        ui_file.open(QFile.ReadOnly)
        loader = QUiLoader()
        self.ui = loader.load(ui_file, self)

        global ui
        ui = self.ui

        title = "Material Properties"
        self.setWindowTitle(title)


        # ////////////////////////////////////////////  

        # Conections
        ExcelFile = pd.ExcelFile(path)
        sheets = ExcelFile.sheet_names
        for sheet in sheets: 
            ui.MatSelectBox.addItem(sheet)
            
        ui.MatSelectBox.addItem("New Material")
        
        

        ui.MatSelectBox.currentIndexChanged.connect(lambda: self.loadPropertiesDF(ui.MatSelectBox.currentIndex(), ExcelFile, ui.PropertiesTable))
        

    
    def loadPropertiesDF(self, sheet_index:int, file: pd.ExcelFile, table: QTableWidget) -> None:
        "This function loads the properties of a pandas dataframe into a qtablewidget"    
        ChosenMaterialDF = file.parse(sheet_name=sheet_index)
        headers = list(ChosenMaterialDF)
        table.setColumnCount(ChosenMaterialDF.shape[1]) 
        table.setRowCount(ChosenMaterialDF.shape[0])
        table.setHorizontalHeaderLabels(headers)

        df_array = ChosenMaterialDF.values
        for i in range(ChosenMaterialDF.shape[0]):
            for j in range(ChosenMaterialDF.shape[1]):
                table.setItem(i, j, QTableWidgetItem(str(df_array[i, j])))
        
        
        
        