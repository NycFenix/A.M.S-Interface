import os
import sys
#from AMSInterface_atual import Ui_AMS_Interface
from lib.ui import Ui_AMS_Interface
from AMSInterface import AMSInterface
from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QCheckBox, QDial, QGridLayout,
    QLabel, QLayout, QLineEdit, QMainWindow,
    QPushButton, QSizePolicy, QSpacerItem, QTabWidget,
    QVBoxLayout, QWidget)



if __name__ == "__main__":
    app = QApplication(sys.argv)
    QUI = QMainWindow()
    ui = Ui_AMS_Interface()
    ui.setupUi(QUI)
    QUI.show()
    sys.exit(app.exec())




