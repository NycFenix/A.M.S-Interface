from Interface import *
from PySide6.QtWidgets import QApplication, QMainWindow
import sys
if __name__ == "__main__":

    app = QApplication(sys.argv)
    QUI = QMainWindow()
    ui = Ui_AMS()
    ui.setupUi(QUI)
    QUI.show()
    sys.exit(app.exec())
