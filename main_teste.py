from Interface import *
from PySide6.QtWidgets import QApplication, QMainWindow
from PySide6.QtGui import QPalette
import sys

def paletteConfig(aplication = QApplication):
    palette = aplication.palette()
    palette.setColor(QPalette.Window, QColor(100, 200, 0))
    palette.setColor(QPalette.Button, QColor(0, 200, 200))

    
    aplication.setPalette(palette)
if __name__ == "__main__":

    app = QApplication(sys.argv)

    paletteConfig(app)
    QUI = QMainWindow()
    ui = Ui_AMS()
    ui.setupUi(QUI)
    QUI.show()
    sys.exit(app.exec())
