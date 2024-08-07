# from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
#     QMetaObject, QObject, QPoint, QRect,
#     QSize, QTime, QUrl, Qt)
# from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
#     QFont, QFontDatabase, QGradient, QIcon,
#     QImage, QKeySequence, QLinearGradient, QPainter,
#     QPalette, QPixmap, QRadialGradient, QTransform, QPen)
# from PySide6.QtWidgets import (QApplication, QMainWindow, QSizePolicy, QTabWidget,
#     QWidget, QGridLayout)

# import os
# import sys

# class Ui_MainWindow(object):
#     def setupUi(self, MainWindow):
#         if not MainWindow.objectName():
#             MainWindow.setObjectName(u"MainWindow")
#         MainWindow.resize(800, 600)
       


#         # Initial Widget Definition

#         ## Main Tabs
#         self.centralwidget = QWidget(MainWindow)
#         self.primaryTabWidget = QTabWidget(self.centralwidget)
#         self.tab = QWidget()
#         self.tab_2 = QWidget()
#         self.tab_3 = QWidget()
#         self.tab_4 = QWidget()
#         self.tab_5 = QWidget()
#         self.tab_6 = QWidget()


#         self.PredictionSubTabWidget = QTabWidget(self.tab)
#         self.PredictionSubTabWidget.setGeometry(QRect(0, 0, 800, 570))
#         self.tab.layout = QGridLayout(self.tab)
#         self.tab.layout.addWidget(self.PredictionSubTabWidget)
#         self.tab.setLayout(self.tab.layout)

#         self.MeasuringToolSubTabWidget = QTabWidget(self.tab_2)
#         self.tab_2.layout = QGridLayout(self.tab_2)
#         self.tab_2.layout.addWidget(self.MeasuringToolSubTabWidget)
#         self.tab_2.setLayout(self.tab_2.layout)


#         ## Prediction widgets
#         self.geometria_cordao = QWidget()
#         self.gc_layout_widget = QWidget(self.geometria_cordao)
#         self.gc_layout_widget.setGeometry(QRect(0, 0, 760, 540))
#         self.GC_Layout = QGridLayout(self.gc_layout_widget)
#         self.geometria_cordao.setLayout(self.GC_Layout)

#         self.altura_camadas = QWidget()

#         self.redes_neurais_geometria = QWidget()
#         self.balanco_fase = QWidget()
#         self.distancia_interdendritica = QWidget()
#         self.tamanho_grao = QWidget()

#         ##Measuring Tool tabs
#         self.melting_pool = QWidget()
#         self.bead_geometry = QWidget()

        
#         self.primaryTabWidget.setGeometry(QRect(0, 0, 800, 600))
        
#         # Red_Palette for primary tab
#         red_palette = QPalette()
#         red_brush = QBrush(QColor(255, 0, 0, 255))
#         red_brush.setStyle(Qt.SolidPattern)
#         red_palette.setBrush(QPalette.Active, QPalette.WindowText, red_brush)
#         self.primaryTabWidget.setPalette(red_palette)
        
#         # Blue_Pallete for secondary tabs
#         blue_palette = QPalette()
#         blue_brush = QBrush(QColor(0, 0, 0, 0))
#         blue_brush.setStyle(Qt.SolidPattern)
#         blue_palette.setBrush(QPalette.Active, QPalette.WindowText, blue_brush)
#         self.PredictionSubTabWidget.setPalette(blue_palette)

#         # Adding tabs
#         self.tab.setMinimumSize(QSize(0, 452))
#         self.primaryTabWidget.addTab(self.tab_2, "")
#         self.primaryTabWidget.addTab(self.tab_3, "")
#         self.primaryTabWidget.addTab(self.tab_4, "")
#         self.primaryTabWidget.addTab(self.tab_5, "")
#         self.primaryTabWidget.addTab(self.tab_6, "")
        
#         self.PredictionSubTabWidget.addTab(self.geometria_cordao, "Geometria do cordão")
#         self.PredictionSubTabWidget.addTab(self.altura_camadas, "Altura das camadas ")
        

#         # Predicition Fields
#         reddish_pink = QColor(214, 118, 118)
#         salmon = QColor(245, 232, 220)
#         light orange = QColor(240, 222, 201)
#         orange = QColor(245, 173, 125)
#         light_brown = QColor(232, 181, 146)
#         winecolor = QColor(162, 23, 51)
#         light_Salmon = QColor(240, 149, 149)
#         light_blue_Button = QColor(197, 252, 252)

#         electric_parameter = QRect()
#         electric_current = QRect()
#         physical_properties = QRect()
#         geometrical_prediction = QRect()
#         wire_characteristics = QRect()
#         geometric_prediction_different_layers = QRect()
        
#         # Final settings
#         MainWindow.setCentralWidget(self.centralwidget)
#         self.retranslateUi(MainWindow)
#         self.primaryTabWidget.setCurrentIndex(0)


#         QMetaObject.connectSlotsByName(MainWindow)
#     # setupUi

#     def retranslateUi(self, MainWindow):
#         MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
#         self.primaryTabWidget.setTabText(self.primaryTabWidget.indexOf(self.tab), QCoreApplication.translate("MainWindow", u"Predi\u00e7\u00e3o", None))
#         self.primaryTabWidget.setTabText(self.primaryTabWidget.indexOf(self.tab_2), QCoreApplication.translate("MainWindow", u"Measuring Tool", None))
#         self.primaryTabWidget.setTabText(self.primaryTabWidget.indexOf(self.tab_3), QCoreApplication.translate("MainWindow", u"Thermal Cycles", None))
#         self.primaryTabWidget.setTabText(self.primaryTabWidget.indexOf(self.tab_4), QCoreApplication.translate("MainWindow", u"Point Cloud Analysis", None))
#         self.primaryTabWidget.setTabText(self.primaryTabWidget.indexOf(self.tab_5), QCoreApplication.translate("MainWindow", u"Thermal control systems", None))
#         self.primaryTabWidget.setTabText(self.primaryTabWidget.indexOf(self.tab_6), QCoreApplication.translate("MainWindow", u"Instability and detect monitoring", None))

#         self.PredictionSubTabWidget.setTabText(self.PredictionSubTabWidget.indexOf(self.geometria_cordao), QCoreApplication.translate("MainWindow", "Geometria do cordão", None))
#         self.PredictionSubTabWidget.setTabText(self.PredictionSubTabWidget.indexOf(self.altura_camadas), QCoreApplication.translate("MainWindow", "Altura das camadas", None))

#     # retranslateUi

# if __name__ == "__main__":
#     app = QApplication(sys.argv)
#     QUI = QMainWindow()
#     ui = Ui_MainWindow()
#     ui.setupUi(QUI)
#     QUI.show()
#     sys.exit(app.exec())


