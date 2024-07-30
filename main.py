from Interface import *
from PySide6.QtWidgets import QApplication, QMainWindow
from PySide6.QtGui import QPalette
import sys
if __name__ == "__main__":

    app = QApplication(sys.argv)

    dark_palette = app.palette()
    dark_palette.setColor(QPalette.Window, QColor(54, 54, 54))
    dark_palette.setColor(QPalette.Button, QColor(0, 200, 200))
    app.setStyle('Fusion')
    app.setPalette(dark_palette)
    QUI = QMainWindow()
    ui = Ui_AMS()
    ui.setupUi(QUI)
    QUI.show()
    sys.exit(app.exec())
