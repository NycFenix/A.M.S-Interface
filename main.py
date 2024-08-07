from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QMainWindow, QSizePolicy, QTabWidget,
    QWidget)

import os
import sys

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(800, 600)
        MainWindow.setUnifiedTitleAndToolBarOnMac(False)
        self.centralwidget = QWidget(MainWindow)

        self.primaryTabWidget = QTabWidget(self.centralwidget)

        self.primaryTabWidget.setGeometry(QRect(0, 0, 800, 600))
        palette = QPalette()
        brush = QBrush(QColor(255, 0, 0, 255))
        brush.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.WindowText, brush)
        brush1 = QBrush(QColor(0, 0, 0, 255))
        brush1.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.ToolTipText, brush1)
        palette.setBrush(QPalette.Inactive, QPalette.WindowText, brush)
        palette.setBrush(QPalette.Inactive, QPalette.ToolTipText, brush1)
        palette.setBrush(QPalette.Disabled, QPalette.ToolTipText, brush1)
        self.primaryTabWidget.setPalette(palette)
        self.tab = QWidget()
        
        self.tab.setMinimumSize(QSize(0, 452))
        
        self.tab_2 = QWidget()
        
        self.primaryTabWidget.addTab(self.tab_2, "")
        self.tab_3 = QWidget()
        
        self.primaryTabWidget.addTab(self.tab_3, "")
        self.tab_4 = QWidget()
      
        self.primaryTabWidget.addTab(self.tab_4, "")
        self.tab_5 = QWidget()
        self.primaryTabWidget.addTab(self.tab_5, "")
        self.tab_6 = QWidget()
      
        self.primaryTabWidget.addTab(self.tab_6, "")
        MainWindow.setCentralWidget(self.centralwidget)




        self.retranslateUi(MainWindow)
        self.primaryTabWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.primaryTabWidget.setTabText(self.primaryTabWidget.indexOf(self.tab), QCoreApplication.translate("MainWindow", u"Predi\u00e7\u00e3o", None))
        self.primaryTabWidget.setTabText(self.primaryTabWidget.indexOf(self.tab_2), QCoreApplication.translate("MainWindow", u"Measuring Tool", None))
        self.primaryTabWidget.setTabText(self.primaryTabWidget.indexOf(self.tab_3), QCoreApplication.translate("MainWindow", u"Thermal Cycles", None))
        self.primaryTabWidget.setTabText(self.primaryTabWidget.indexOf(self.tab_4), QCoreApplication.translate("MainWindow", u"Point Cloud Analysis", None))
        self.primaryTabWidget.setTabText(self.primaryTabWidget.indexOf(self.tab_5), QCoreApplication.translate("MainWindow", u"Thermal control systems", None))
        self.primaryTabWidget.setTabText(self.primaryTabWidget.indexOf(self.tab_6), QCoreApplication.translate("MainWindow", u"Instability and detect monitoring", None))
    # retranslateUi

if __name__ == "__main__":
    app = QApplication(sys.argv)
    QUI = QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(QUI)
    QUI.show()
    sys.exit(app.exec())