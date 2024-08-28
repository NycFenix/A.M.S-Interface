import os
import sys
#from AMSInterface_atual import Ui_AMS_Interface
#from lib.ui import Ui_AMS_Interface
from AMSInterface import AMSInterface


from PySide6.QtWidgets import (QApplication, QCheckBox, QDial, QGridLayout,
    QLabel, QLayout, QLineEdit, QMainWindow,
    QPushButton, QSizePolicy, QSpacerItem, QTabWidget,
    QVBoxLayout, QWidget)

from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    app.setWindowIcon(QIcon("img/sold_icon.ico"))
    
    #ui = Ui_AMS_Interface()
    ui = AMSInterface()
    #ui.setupUi(QUI)
    
    sys.exit(app.exec())




