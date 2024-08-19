# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'AMSInterface.ui'
##
## Created by: Qt User Interface Compiler version 6.4.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

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

from include import BeadGeometry

class Ui_AMS_Interface(object):
    def setupUi(self, AMS_Interface):
        if not AMS_Interface.objectName():
            AMS_Interface.setObjectName(u"AMS_Interface")
        AMS_Interface.resize(814, 624)
        palette = QPalette()
        brush1 = QBrush(QColor(255, 255, 255, 255))
        brush1.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Window, brush1)
        palette.setBrush(QPalette.Inactive, QPalette.Window, brush1)
        palette.setBrush(QPalette.Disabled, QPalette.Base, brush1)
        palette.setBrush(QPalette.Disabled, QPalette.Window, brush1)
        AMS_Interface.setPalette(palette)
        AMS_Interface.setUnifiedTitleAndToolBarOnMac(False)
        self.centralwidget = QWidget(AMS_Interface)
        self.centralwidget.setObjectName(u"centralwidget")


        self.primaryTabWidget = QTabWidget(self.centralwidget)
        self.primaryTabWidget.setObjectName(u"primaryTabWidget")
        self.primaryTabWidget.setGeometry(QRect(9, 9, 800, 600))


        palette1 = QPalette()
        brush2 = QBrush(QColor(255, 0, 0, 255))
        brush2.setStyle(Qt.SolidPattern)
        palette1.setBrush(QPalette.Active, QPalette.WindowText, brush2)
        brush3 = QBrush(QColor(0, 0, 0, 255))
        brush3.setStyle(Qt.SolidPattern)
        palette1.setBrush(QPalette.Active, QPalette.ToolTipText, brush3)
        palette1.setBrush(QPalette.Inactive, QPalette.WindowText, brush2)
        palette1.setBrush(QPalette.Inactive, QPalette.ToolTipText, brush3)
        palette1.setBrush(QPalette.Disabled, QPalette.ToolTipText, brush3)
        self.primaryTabWidget.setPalette(palette1)
        self.PredictionWidget = QWidget()
        self.PredictionWidget.setObjectName(u"PredictionWidget")
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.PredictionWidget.sizePolicy().hasHeightForWidth())
        self.PredictionWidget.setSizePolicy(sizePolicy)
        self.PredictionWidget.setMinimumSize(QSize(0, 452))
        palette2 = QPalette()
        brush4 = QBrush(QColor(214, 118, 118, 255))
        brush4.setStyle(Qt.SolidPattern)
        palette2.setBrush(QPalette.Active, QPalette.Base, brush4)
        palette2.setBrush(QPalette.Active, QPalette.Window, brush4)
        palette2.setBrush(QPalette.Inactive, QPalette.Base, brush4)
        palette2.setBrush(QPalette.Inactive, QPalette.Window, brush4)
        palette2.setBrush(QPalette.Disabled, QPalette.Base, brush4)
        palette2.setBrush(QPalette.Disabled, QPalette.Window, brush4)
        self.PredictionWidget.setPalette(palette2)
        self.verticalLayout_3 = QVBoxLayout(self.PredictionWidget)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.PredictionSubTabWidget = QTabWidget(self.PredictionWidget)
        self.PredictionSubTabWidget.setObjectName(u"PredictionSubTabWidget")
        palette3 = QPalette()
        brush5 = QBrush(QColor(0, 0, 255, 255))
        brush5.setStyle(Qt.SolidPattern)
        palette3.setBrush(QPalette.Active, QPalette.WindowText, brush5)
        palette3.setBrush(QPalette.Active, QPalette.Base, brush1)
        palette3.setBrush(QPalette.Active, QPalette.Window, brush1)
        palette3.setBrush(QPalette.Inactive, QPalette.WindowText, brush5)
        palette3.setBrush(QPalette.Inactive, QPalette.Base, brush1)
        palette3.setBrush(QPalette.Inactive, QPalette.Window, brush1)
        palette3.setBrush(QPalette.Disabled, QPalette.Base, brush1)
        palette3.setBrush(QPalette.Disabled, QPalette.Window, brush1)
        self.PredictionSubTabWidget.setPalette(palette3)
        self.Geometriadocordao = QWidget()
        self.Geometriadocordao.setObjectName(u"Geometriadocordao")
        palette4 = QPalette()
        palette4.setBrush(QPalette.Active, QPalette.WindowText, brush5)
        palette4.setBrush(QPalette.Active, QPalette.Button, brush4)
        palette4.setBrush(QPalette.Active, QPalette.Base, brush4)
        palette4.setBrush(QPalette.Active, QPalette.Window, brush4)
        palette4.setBrush(QPalette.Inactive, QPalette.WindowText, brush5)
        palette4.setBrush(QPalette.Inactive, QPalette.Button, brush4)
        palette4.setBrush(QPalette.Inactive, QPalette.Base, brush4)
        palette4.setBrush(QPalette.Inactive, QPalette.Window, brush4)
        palette4.setBrush(QPalette.Disabled, QPalette.Button, brush4)
        palette4.setBrush(QPalette.Disabled, QPalette.Base, brush4)
        palette4.setBrush(QPalette.Disabled, QPalette.Window, brush4)


        # all rects have to be before all labels
        self.rectEP = QLabel(self.Geometriadocordao)
        self.rectEP.setObjectName(u"rectEP")
        self.rectEP.setStyleSheet(u"#rectEP {\n""background-color:rgb(245, 232, 220)\n""}")

        self.rectEP.setGeometry(QRect(5, 5, 260, 235))

        self.rectEC = QLabel(self.Geometriadocordao)
        self.rectEC.setObjectName(u"rectEC")
        self.rectEC.setStyleSheet(u"#rectEC {\n""background-color:rgb(245, 232, 220)\n""}")
        self.rectEC.setGeometry(QRect(5, 245, 350, 100))

        self.rect3 = QLabel(self.Geometriadocordao)
        self.rect3.setObjectName(u"rect3")
        self.rect3.setStyleSheet(u"#rect3 {\n""background-color:rgb(245, 232, 220)\n""}")
        self.rect3.setGeometry(QRect(5, 350, 370, 185))

        self.rect4 = QLabel(self.Geometriadocordao)
        self.rect4.setObjectName(u"rect4")
        self.rect4.setStyleSheet(u"#rect4 {\n""background-color:rgb(245, 232, 220)\n""}")
        self.rect4.setGeometry(QRect(375, 245, 200, 100))

        self.rect5 = QLabel(self.Geometriadocordao)
        self.rect5.setObjectName("rect5")
        self.rect5.setStyleSheet(u"#rect5 {\n""background-color:rgb(245, 232, 220)\n""}")
        self.rect5.setGeometry(QRect(380, 350, 405, 185))

        self.rect6 = QLabel(self.Geometriadocordao)
        self.rect6.setObjectName("rect6")
        self.rect6.setStyleSheet(u"#rect6 {\n""background-color:rgb(245, 232, 220)\n""}")
        self.rect6.setGeometry(QRect(580, 5, 205, 350))

        self.Geometriadocordao.setPalette(palette4)
        self.Geometriadocordao.setStyleSheet(u"#Geometriadocordao{\n"
"	background: rgb(214, 118, 118);\n"
"}")
        
        
        self.gridLayout_4 = QGridLayout(self.Geometriadocordao)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.gridLayout_4.setHorizontalSpacing(5)
        self.gridLayout_4.setVerticalSpacing(10)
        self.gridLayout_4.setContentsMargins(-1, 10, 5, 10)
        self.electric_current_layout = QGridLayout()
        self.electric_current_layout.setObjectName(u"electric_current_layout")
        self.electric_current_layout.setHorizontalSpacing(10)
        self.electric_current_layout.setVerticalSpacing(5)
        self.electric_current_layout.setContentsMargins(10, -1, -1, 10)
        self.current_label = QLabel(self.Geometriadocordao)
        self.current_label.setObjectName(u"current_label")
        palette5 = QPalette()
        palette5.setBrush(QPalette.Active, QPalette.WindowText, brush1)
        brush6 = QBrush(QColor(245, 132, 153, 255))
        brush6.setStyle(Qt.SolidPattern)
        palette5.setBrush(QPalette.Active, QPalette.Button, brush6)
        palette5.setBrush(QPalette.Active, QPalette.Base, brush6)
        palette5.setBrush(QPalette.Active, QPalette.Window, brush6)
        palette5.setBrush(QPalette.Inactive, QPalette.WindowText, brush1)
        palette5.setBrush(QPalette.Inactive, QPalette.Button, brush6)
        palette5.setBrush(QPalette.Inactive, QPalette.Base, brush6)
        palette5.setBrush(QPalette.Inactive, QPalette.Window, brush6)
        palette5.setBrush(QPalette.Disabled, QPalette.Button, brush6)
        palette5.setBrush(QPalette.Disabled, QPalette.Base, brush6)
        palette5.setBrush(QPalette.Disabled, QPalette.Window, brush6)
        self.current_label.setPalette(palette5)
        font = QFont()
        font.setBold(True)
        self.current_label.setFont(font)
        self.current_label.setStyleSheet(u"background-color:rgb(245, 132, 153)")

        self.electric_current_layout.addWidget(self.current_label, 2, 3, 1, 3)

        self.current_title = QLabel(self.Geometriadocordao)
        self.current_title.setObjectName(u"current_title")
        palette6 = QPalette()
        brush7 = QBrush(QColor(162, 23, 51, 255))
        brush7.setStyle(Qt.SolidPattern)
        palette6.setBrush(QPalette.Active, QPalette.WindowText, brush7)
        palette6.setBrush(QPalette.Inactive, QPalette.WindowText, brush7)
        self.current_title.setPalette(palette6)
        font1 = QFont()
        font1.setPointSize(8)
        font1.setBold(False)
        self.current_title.setFont(font1)

        self.electric_current_layout.addWidget(self.current_title, 0, 0, 1, 3)

        self.I_spacer = QSpacerItem(20, 50, QSizePolicy.Minimum, QSizePolicy.Minimum)

        self.electric_current_layout.addItem(self.I_spacer, 4, 1, 1, 1)

        self.viscosity = QLineEdit(self.Geometriadocordao)
        self.viscosity.setObjectName(u"viscosity")

        self.electric_current_layout.addWidget(self.viscosity, 11, 1, 1, 1)

        self.melting_point_label_2 = QLabel(self.Geometriadocordao)
        self.melting_point_label_2.setObjectName(u"melting_point_label_2")
        palette7 = QPalette()
        palette7.setBrush(QPalette.Active, QPalette.WindowText, brush3)
        palette7.setBrush(QPalette.Inactive, QPalette.WindowText, brush3)
        self.melting_point_label_2.setPalette(palette7)
        font2 = QFont()
        font2.setItalic(False)
        self.melting_point_label_2.setFont(font2)
        self.melting_point_label_2.setAlignment(Qt.AlignCenter)

        self.electric_current_layout.addWidget(self.melting_point_label_2, 7, 2, 1, 1)

        self.specific_heat_label_2 = QLabel(self.Geometriadocordao)
        self.specific_heat_label_2.setObjectName(u"specific_heat_label_2")
        palette8 = QPalette()
        palette8.setBrush(QPalette.Active, QPalette.WindowText, brush3)
        palette8.setBrush(QPalette.Inactive, QPalette.WindowText, brush3)
        self.specific_heat_label_2.setPalette(palette8)

        self.electric_current_layout.addWidget(self.specific_heat_label_2, 9, 2, 1, 1)

        self.fronius_current = QLineEdit(self.Geometriadocordao)
        self.fronius_current.setObjectName(u"fronius_current")

        self.electric_current_layout.addWidget(self.fronius_current, 2, 1, 1, 2)

        self.density_measure = QLabel(self.Geometriadocordao)
        self.density_measure.setObjectName(u"density_measure")
        palette9 = QPalette()
        palette9.setBrush(QPalette.Active, QPalette.WindowText, brush3)
        palette9.setBrush(QPalette.Inactive, QPalette.WindowText, brush3)
        self.density_measure.setPalette(palette9)
        self.density_measure.setAlignment(Qt.AlignCenter)

        self.electric_current_layout.addWidget(self.density_measure, 7, 6, 1, 1)

        self.viscosity_label = QLabel(self.Geometriadocordao)
        self.viscosity_label.setObjectName(u"viscosity_label")
        palette10 = QPalette()
        palette10.setBrush(QPalette.Active, QPalette.WindowText, brush1)
        palette10.setBrush(QPalette.Active, QPalette.Button, brush6)
        palette10.setBrush(QPalette.Active, QPalette.Base, brush6)
        palette10.setBrush(QPalette.Active, QPalette.Window, brush6)
        palette10.setBrush(QPalette.Inactive, QPalette.WindowText, brush1)
        palette10.setBrush(QPalette.Inactive, QPalette.Button, brush6)
        palette10.setBrush(QPalette.Inactive, QPalette.Base, brush6)
        palette10.setBrush(QPalette.Inactive, QPalette.Window, brush6)
        palette10.setBrush(QPalette.Disabled, QPalette.Button, brush6)
        palette10.setBrush(QPalette.Disabled, QPalette.Base, brush6)
        palette10.setBrush(QPalette.Disabled, QPalette.Window, brush6)
        self.viscosity_label.setPalette(palette10)
        font3 = QFont()
        font3.setPointSize(7)
        font3.setBold(True)
        self.viscosity_label.setFont(font3)
        self.viscosity_label.setStyleSheet(u"background-color:rgb(245, 132, 153)")

        self.electric_current_layout.addWidget(self.viscosity_label, 10, 1, 1, 1)

        self.thermal_conductivity = QLineEdit(self.Geometriadocordao)
        self.thermal_conductivity.setObjectName(u"thermal_conductivity")

        self.electric_current_layout.addWidget(self.thermal_conductivity, 9, 4, 1, 2)

        self.emissivity = QLineEdit(self.Geometriadocordao)
        self.emissivity.setObjectName(u"emissivity")

        self.electric_current_layout.addWidget(self.emissivity, 11, 4, 1, 2)

        self.specific_heat = QLineEdit(self.Geometriadocordao)
        self.specific_heat.setObjectName(u"specific_heat")

        self.electric_current_layout.addWidget(self.specific_heat, 9, 1, 1, 1)

        self.conductivity_label_2 = QLabel(self.Geometriadocordao)
        self.conductivity_label_2.setObjectName(u"conductivity_label_2")
        sizePolicy1 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy1.setHorizontalStretch(10)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.conductivity_label_2.sizePolicy().hasHeightForWidth())
        self.conductivity_label_2.setSizePolicy(sizePolicy1)
        palette11 = QPalette()
        palette11.setBrush(QPalette.Active, QPalette.WindowText, brush3)
        brush8 = QBrush(QColor(245, 230, 196, 255))
        brush8.setStyle(Qt.SolidPattern)
        palette11.setBrush(QPalette.Active, QPalette.Button, brush8)
        palette11.setBrush(QPalette.Active, QPalette.Base, brush8)
        palette11.setBrush(QPalette.Active, QPalette.Window, brush8)
        palette11.setBrush(QPalette.Inactive, QPalette.WindowText, brush3)
        palette11.setBrush(QPalette.Inactive, QPalette.Button, brush8)
        palette11.setBrush(QPalette.Inactive, QPalette.Base, brush8)
        palette11.setBrush(QPalette.Inactive, QPalette.Window, brush8)
        palette11.setBrush(QPalette.Disabled, QPalette.Button, brush8)
        palette11.setBrush(QPalette.Disabled, QPalette.Base, brush8)
        palette11.setBrush(QPalette.Disabled, QPalette.Window, brush8)
        self.conductivity_label_2.setPalette(palette11)
        font4 = QFont()
        font4.setBold(True)
        font4.setItalic(False)
        self.conductivity_label_2.setFont(font4)
        self.conductivity_label_2.setStyleSheet(u"background-color:rgb(245, 230, 196)")
        self.conductivity_label_2.setAlignment(Qt.AlignCenter)

        self.electric_current_layout.addWidget(self.conductivity_label_2, 9, 3, 1, 1)

        self.viscosity_icon = QLabel(self.Geometriadocordao)
        self.viscosity_icon.setObjectName(u"viscosity_icon")
        sizePolicy1.setHeightForWidth(self.viscosity_icon.sizePolicy().hasHeightForWidth())
        self.viscosity_icon.setSizePolicy(sizePolicy1)
        palette12 = QPalette()
        palette12.setBrush(QPalette.Active, QPalette.WindowText, brush3)
        palette12.setBrush(QPalette.Active, QPalette.Button, brush8)
        palette12.setBrush(QPalette.Active, QPalette.Base, brush8)
        palette12.setBrush(QPalette.Active, QPalette.Window, brush8)
        palette12.setBrush(QPalette.Inactive, QPalette.WindowText, brush3)
        palette12.setBrush(QPalette.Inactive, QPalette.Button, brush8)
        palette12.setBrush(QPalette.Inactive, QPalette.Base, brush8)
        palette12.setBrush(QPalette.Inactive, QPalette.Window, brush8)
        palette12.setBrush(QPalette.Disabled, QPalette.Button, brush8)
        palette12.setBrush(QPalette.Disabled, QPalette.Base, brush8)
        palette12.setBrush(QPalette.Disabled, QPalette.Window, brush8)
        self.viscosity_icon.setPalette(palette12)
        self.viscosity_icon.setFont(font4)
        self.viscosity_icon.setStyleSheet(u"background-color:rgb(245, 230, 196)")

        self.electric_current_layout.addWidget(self.viscosity_icon, 11, 0, 1, 1)

        self.conductivity_label = QLabel(self.Geometriadocordao)
        self.conductivity_label.setObjectName(u"conductivity_label")
        palette13 = QPalette()
        palette13.setBrush(QPalette.Active, QPalette.WindowText, brush1)
        palette13.setBrush(QPalette.Active, QPalette.Button, brush6)
        palette13.setBrush(QPalette.Active, QPalette.Base, brush6)
        palette13.setBrush(QPalette.Active, QPalette.Window, brush6)
        palette13.setBrush(QPalette.Inactive, QPalette.WindowText, brush1)
        palette13.setBrush(QPalette.Inactive, QPalette.Button, brush6)
        palette13.setBrush(QPalette.Inactive, QPalette.Base, brush6)
        palette13.setBrush(QPalette.Inactive, QPalette.Window, brush6)
        palette13.setBrush(QPalette.Disabled, QPalette.Button, brush6)
        palette13.setBrush(QPalette.Disabled, QPalette.Base, brush6)
        palette13.setBrush(QPalette.Disabled, QPalette.Window, brush6)
        self.conductivity_label.setPalette(palette13)
        self.conductivity_label.setFont(font3)
        self.conductivity_label.setStyleSheet(u"background-color:rgb(245, 132, 153)")

        self.electric_current_layout.addWidget(self.conductivity_label, 8, 4, 1, 2)

        self.density_label = QLabel(self.Geometriadocordao)
        self.density_label.setObjectName(u"density_label")
        palette14 = QPalette()
        palette14.setBrush(QPalette.Active, QPalette.WindowText, brush1)
        palette14.setBrush(QPalette.Active, QPalette.Button, brush6)
        palette14.setBrush(QPalette.Active, QPalette.Base, brush6)
        palette14.setBrush(QPalette.Active, QPalette.Window, brush6)
        palette14.setBrush(QPalette.Inactive, QPalette.WindowText, brush1)
        palette14.setBrush(QPalette.Inactive, QPalette.Button, brush6)
        palette14.setBrush(QPalette.Inactive, QPalette.Base, brush6)
        palette14.setBrush(QPalette.Inactive, QPalette.Window, brush6)
        palette14.setBrush(QPalette.Disabled, QPalette.Button, brush6)
        palette14.setBrush(QPalette.Disabled, QPalette.Base, brush6)
        palette14.setBrush(QPalette.Disabled, QPalette.Window, brush6)
        self.density_label.setPalette(palette14)
        self.density_label.setFont(font3)
        self.density_label.setStyleSheet(u"background-color:rgb(245, 132, 153)")
        self.density_label.setAlignment(Qt.AlignCenter)

        self.electric_current_layout.addWidget(self.density_label, 6, 4, 1, 2)

        self.specific_heat_label = QLabel(self.Geometriadocordao)
        self.specific_heat_label.setObjectName(u"specific_heat_label")
        palette15 = QPalette()
        palette15.setBrush(QPalette.Active, QPalette.WindowText, brush1)
        palette15.setBrush(QPalette.Active, QPalette.Button, brush6)
        palette15.setBrush(QPalette.Active, QPalette.Base, brush6)
        palette15.setBrush(QPalette.Active, QPalette.Window, brush6)
        palette15.setBrush(QPalette.Inactive, QPalette.WindowText, brush1)
        palette15.setBrush(QPalette.Inactive, QPalette.Button, brush6)
        palette15.setBrush(QPalette.Inactive, QPalette.Base, brush6)
        palette15.setBrush(QPalette.Inactive, QPalette.Window, brush6)
        palette15.setBrush(QPalette.Disabled, QPalette.Button, brush6)
        palette15.setBrush(QPalette.Disabled, QPalette.Base, brush6)
        palette15.setBrush(QPalette.Disabled, QPalette.Window, brush6)
        self.specific_heat_label.setPalette(palette15)
        self.specific_heat_label.setFont(font3)
        self.specific_heat_label.setStyleSheet(u"background-color:rgb(245, 132, 153)")

        self.electric_current_layout.addWidget(self.specific_heat_label, 8, 1, 1, 1)

        self.emissivity_label = QLabel(self.Geometriadocordao)
        self.emissivity_label.setObjectName(u"emissivity_label")
        palette16 = QPalette()
        palette16.setBrush(QPalette.Active, QPalette.WindowText, brush1)
        palette16.setBrush(QPalette.Active, QPalette.Button, brush6)
        palette16.setBrush(QPalette.Active, QPalette.Base, brush6)
        palette16.setBrush(QPalette.Active, QPalette.Window, brush6)
        palette16.setBrush(QPalette.Inactive, QPalette.WindowText, brush1)
        palette16.setBrush(QPalette.Inactive, QPalette.Button, brush6)
        palette16.setBrush(QPalette.Inactive, QPalette.Base, brush6)
        palette16.setBrush(QPalette.Inactive, QPalette.Window, brush6)
        palette16.setBrush(QPalette.Disabled, QPalette.Button, brush6)
        palette16.setBrush(QPalette.Disabled, QPalette.Base, brush6)
        palette16.setBrush(QPalette.Disabled, QPalette.Window, brush6)
        self.emissivity_label.setPalette(palette16)
        self.emissivity_label.setFont(font3)
        self.emissivity_label.setStyleSheet(u"background-color:rgb(245, 132, 153)")
        self.emissivity_label.setAlignment(Qt.AlignCenter)

        self.electric_current_layout.addWidget(self.emissivity_label, 10, 4, 1, 2)

        self.emissivity_icon = QLabel(self.Geometriadocordao)
        self.emissivity_icon.setObjectName(u"emissivity_icon")
        sizePolicy1.setHeightForWidth(self.emissivity_icon.sizePolicy().hasHeightForWidth())
        self.emissivity_icon.setSizePolicy(sizePolicy1)
        palette17 = QPalette()
        palette17.setBrush(QPalette.Active, QPalette.WindowText, brush3)
        palette17.setBrush(QPalette.Active, QPalette.Button, brush8)
        palette17.setBrush(QPalette.Active, QPalette.Base, brush8)
        palette17.setBrush(QPalette.Active, QPalette.Window, brush8)
        palette17.setBrush(QPalette.Inactive, QPalette.WindowText, brush3)
        palette17.setBrush(QPalette.Inactive, QPalette.Button, brush8)
        palette17.setBrush(QPalette.Inactive, QPalette.Base, brush8)
        palette17.setBrush(QPalette.Inactive, QPalette.Window, brush8)
        palette17.setBrush(QPalette.Disabled, QPalette.Button, brush8)
        palette17.setBrush(QPalette.Disabled, QPalette.Base, brush8)
        palette17.setBrush(QPalette.Disabled, QPalette.Window, brush8)
        self.emissivity_icon.setPalette(palette17)
        self.emissivity_icon.setFont(font4)
        self.emissivity_icon.setStyleSheet(u"background-color:rgb(245, 230, 196)")

        self.electric_current_layout.addWidget(self.emissivity_icon, 11, 3, 1, 1)

        self.melting_point_label = QLabel(self.Geometriadocordao)
        self.melting_point_label.setObjectName(u"melting_point_label")
        palette18 = QPalette()
        palette18.setBrush(QPalette.Active, QPalette.WindowText, brush1)
        palette18.setBrush(QPalette.Active, QPalette.Button, brush6)
        palette18.setBrush(QPalette.Active, QPalette.Base, brush6)
        palette18.setBrush(QPalette.Active, QPalette.Window, brush6)
        palette18.setBrush(QPalette.Inactive, QPalette.WindowText, brush1)
        palette18.setBrush(QPalette.Inactive, QPalette.Button, brush6)
        palette18.setBrush(QPalette.Inactive, QPalette.Base, brush6)
        palette18.setBrush(QPalette.Inactive, QPalette.Window, brush6)
        palette18.setBrush(QPalette.Disabled, QPalette.Button, brush6)
        palette18.setBrush(QPalette.Disabled, QPalette.Base, brush6)
        palette18.setBrush(QPalette.Disabled, QPalette.Window, brush6)
        self.melting_point_label.setPalette(palette18)
        self.melting_point_label.setFont(font3)
        self.melting_point_label.setStyleSheet(u"background-color:rgb(245, 132, 153)")

        self.electric_current_layout.addWidget(self.melting_point_label, 6, 1, 1, 1)

        self.I_measure = QLabel(self.Geometriadocordao)
        self.I_measure.setObjectName(u"I_measure")
        palette19 = QPalette()
        palette19.setBrush(QPalette.Active, QPalette.WindowText, brush3)
        palette19.setBrush(QPalette.Inactive, QPalette.WindowText, brush3)
        self.I_measure.setPalette(palette19)
        self.I_measure.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.electric_current_layout.addWidget(self.I_measure, 3, 6, 1, 1)

        self.density = QLineEdit(self.Geometriadocordao)
        self.density.setObjectName(u"density")

        self.electric_current_layout.addWidget(self.density, 7, 4, 1, 2)

        self.I = QLineEdit(self.Geometriadocordao)
        self.I.setObjectName(u"I")

        self.electric_current_layout.addWidget(self.I, 3, 3, 1, 3)

        self.specific_heat_icon = QLabel(self.Geometriadocordao)
        self.specific_heat_icon.setObjectName(u"specific_heat_icon")
        sizePolicy1.setHeightForWidth(self.specific_heat_icon.sizePolicy().hasHeightForWidth())
        self.specific_heat_icon.setSizePolicy(sizePolicy1)
        palette20 = QPalette()
        palette20.setBrush(QPalette.Active, QPalette.WindowText, brush3)
        palette20.setBrush(QPalette.Active, QPalette.Button, brush8)
        palette20.setBrush(QPalette.Active, QPalette.Base, brush8)
        palette20.setBrush(QPalette.Active, QPalette.Window, brush8)
        palette20.setBrush(QPalette.Inactive, QPalette.WindowText, brush3)
        palette20.setBrush(QPalette.Inactive, QPalette.Button, brush8)
        palette20.setBrush(QPalette.Inactive, QPalette.Base, brush8)
        palette20.setBrush(QPalette.Inactive, QPalette.Window, brush8)
        palette20.setBrush(QPalette.Disabled, QPalette.Button, brush8)
        palette20.setBrush(QPalette.Disabled, QPalette.Base, brush8)
        palette20.setBrush(QPalette.Disabled, QPalette.Window, brush8)
        self.specific_heat_icon.setPalette(palette20)
        self.specific_heat_icon.setFont(font4)
        self.specific_heat_icon.setStyleSheet(u"background-color:rgb(245, 230, 196)")

        self.electric_current_layout.addWidget(self.specific_heat_icon, 9, 0, 1, 1)

        self.conductivity_measure = QLabel(self.Geometriadocordao)
        self.conductivity_measure.setObjectName(u"conductivity_measure")
        palette21 = QPalette()
        palette21.setBrush(QPalette.Active, QPalette.WindowText, brush3)
        palette21.setBrush(QPalette.Inactive, QPalette.WindowText, brush3)
        self.conductivity_measure.setPalette(palette21)
        self.conductivity_measure.setAlignment(Qt.AlignCenter)

        self.electric_current_layout.addWidget(self.conductivity_measure, 9, 6, 1, 1)

        self.melting_point = QLineEdit(self.Geometriadocordao)
        self.melting_point.setObjectName(u"melting_point")

        self.electric_current_layout.addWidget(self.melting_point, 7, 1, 1, 1)

        self.melting_point_icon = QLabel(self.Geometriadocordao)
        self.melting_point_icon.setObjectName(u"melting_point_icon")
        sizePolicy1.setHeightForWidth(self.melting_point_icon.sizePolicy().hasHeightForWidth())
        self.melting_point_icon.setSizePolicy(sizePolicy1)
        palette22 = QPalette()
        palette22.setBrush(QPalette.Active, QPalette.WindowText, brush3)
        palette22.setBrush(QPalette.Active, QPalette.Button, brush8)
        palette22.setBrush(QPalette.Active, QPalette.Base, brush8)
        palette22.setBrush(QPalette.Active, QPalette.Window, brush8)
        palette22.setBrush(QPalette.Inactive, QPalette.WindowText, brush3)
        palette22.setBrush(QPalette.Inactive, QPalette.Button, brush8)
        palette22.setBrush(QPalette.Inactive, QPalette.Base, brush8)
        palette22.setBrush(QPalette.Inactive, QPalette.Window, brush8)
        palette22.setBrush(QPalette.Disabled, QPalette.Button, brush8)
        palette22.setBrush(QPalette.Disabled, QPalette.Base, brush8)
        palette22.setBrush(QPalette.Disabled, QPalette.Window, brush8)
        self.melting_point_icon.setPalette(palette22)
        self.melting_point_icon.setFont(font4)
        self.melting_point_icon.setStyleSheet(u"background-color:rgb(245, 230, 196)")

        self.electric_current_layout.addWidget(self.melting_point_icon, 7, 0, 1, 1)

        self.Fronius_checkbox = QCheckBox(self.Geometriadocordao)
        self.Fronius_checkbox.setObjectName(u"Fronius_checkbox")
        palette23 = QPalette()
        palette23.setBrush(QPalette.Active, QPalette.WindowText, brush2)
        palette23.setBrush(QPalette.Inactive, QPalette.WindowText, brush2)
        self.Fronius_checkbox.setPalette(palette23)
        font5 = QFont()
        font5.setStyleStrategy(QFont.PreferAntialias)
        self.Fronius_checkbox.setFont(font5)
        self.Fronius_checkbox.setFocusPolicy(Qt.StrongFocus)

        self.electric_current_layout.addWidget(self.Fronius_checkbox, 1, 0, 1, 3)

        self.density_icon = QLabel(self.Geometriadocordao)
        self.density_icon.setObjectName(u"density_icon")
        sizePolicy1.setHeightForWidth(self.density_icon.sizePolicy().hasHeightForWidth())
        self.density_icon.setSizePolicy(sizePolicy1)
        palette24 = QPalette()
        palette24.setBrush(QPalette.Active, QPalette.WindowText, brush3)
        palette24.setBrush(QPalette.Active, QPalette.Button, brush8)
        palette24.setBrush(QPalette.Active, QPalette.Base, brush8)
        palette24.setBrush(QPalette.Active, QPalette.Window, brush8)
        palette24.setBrush(QPalette.Inactive, QPalette.WindowText, brush3)
        palette24.setBrush(QPalette.Inactive, QPalette.Button, brush8)
        palette24.setBrush(QPalette.Inactive, QPalette.Base, brush8)
        palette24.setBrush(QPalette.Inactive, QPalette.Window, brush8)
        palette24.setBrush(QPalette.Disabled, QPalette.Button, brush8)
        palette24.setBrush(QPalette.Disabled, QPalette.Base, brush8)
        palette24.setBrush(QPalette.Disabled, QPalette.Window, brush8)
        self.density_icon.setPalette(palette24)
        self.density_icon.setFont(font4)
        self.density_icon.setStyleSheet(u"background-color:rgb(245, 230, 196)")

        self.electric_current_layout.addWidget(self.density_icon, 7, 3, 1, 1)

        self.Physical_Properties_title = QLabel(self.Geometriadocordao)
        self.Physical_Properties_title.setObjectName(u"Physical_Properties_title")
        palette25 = QPalette()
        palette25.setBrush(QPalette.Active, QPalette.WindowText, brush7)
        palette25.setBrush(QPalette.Inactive, QPalette.WindowText, brush7)
        self.Physical_Properties_title.setPalette(palette25)
        self.Physical_Properties_title.setFont(font1)

        self.electric_current_layout.addWidget(self.Physical_Properties_title, 5, 0, 1, 3)


        self.gridLayout_4.addLayout(self.electric_current_layout, 3, 0, 3, 5)

        self.predicion_layers_layout = QGridLayout()
        self.predicion_layers_layout.setObjectName(u"predicion_layers_layout")
        self.predicion_layers_layout.setSizeConstraint(QLayout.SetNoConstraint)
        self.predicion_layers_layout.setHorizontalSpacing(30)
        self.predicion_layers_layout.setVerticalSpacing(10)
        self.predicion_layers_layout.setContentsMargins(15, 10, 15, 5)
        self.zta_t = QLineEdit(self.Geometriadocordao)
        self.zta_t.setObjectName(u"zta_t")

        self.predicion_layers_layout.addWidget(self.zta_t, 5, 3, 1, 1)

        self.t_substrate = QLineEdit(self.Geometriadocordao)
        self.t_substrate.setObjectName(u"t_substrate")

        self.predicion_layers_layout.addWidget(self.t_substrate, 4, 1, 1, 1)

        self.zta_t_label = QLabel(self.Geometriadocordao)
        self.zta_t_label.setObjectName(u"zta_t_label")
        palette26 = QPalette()
        palette26.setBrush(QPalette.Active, QPalette.WindowText, brush3)
        palette26.setBrush(QPalette.Inactive, QPalette.WindowText, brush3)
        self.zta_t_label.setPalette(palette26)

        self.predicion_layers_layout.addWidget(self.zta_t_label, 5, 2, 1, 1)

        self.Width_T_label = QLabel(self.Geometriadocordao)
        self.Width_T_label.setObjectName(u"Width_T_label")
        palette27 = QPalette()
        palette27.setBrush(QPalette.Active, QPalette.WindowText, brush3)
        palette27.setBrush(QPalette.Inactive, QPalette.WindowText, brush3)
        self.Width_T_label.setPalette(palette27)

        self.predicion_layers_layout.addWidget(self.Width_T_label, 2, 2, 1, 1)

        self.height_t_label = QLabel(self.Geometriadocordao)
        self.height_t_label.setObjectName(u"height_t_label")
        palette28 = QPalette()
        palette28.setBrush(QPalette.Active, QPalette.WindowText, brush3)
        palette28.setBrush(QPalette.Inactive, QPalette.WindowText, brush3)
        self.height_t_label.setPalette(palette28)

        self.predicion_layers_layout.addWidget(self.height_t_label, 3, 2, 1, 1)

        self.height_t = QLineEdit(self.Geometriadocordao)
        self.height_t.setObjectName(u"height_t")

        self.predicion_layers_layout.addWidget(self.height_t, 3, 3, 1, 1)

        self.substrate_l = QLabel(self.Geometriadocordao)
        self.substrate_l.setObjectName(u"substrate_l")
        sizePolicy2 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Minimum)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.substrate_l.sizePolicy().hasHeightForWidth())
        self.substrate_l.setSizePolicy(sizePolicy2)
        self.substrate_l.setMinimumSize(QSize(50, 0))
        palette29 = QPalette()
        palette29.setBrush(QPalette.Active, QPalette.WindowText, brush3)
        palette29.setBrush(QPalette.Inactive, QPalette.WindowText, brush3)
        self.substrate_l.setPalette(palette29)
        font6 = QFont()
        font6.setPointSize(8)
        self.substrate_l.setFont(font6)
        self.substrate_l.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.predicion_layers_layout.addWidget(self.substrate_l, 5, 0, 1, 1)

        self.t_layer = QLineEdit(self.Geometriadocordao)
        self.t_layer.setObjectName(u"t_layer")

        self.predicion_layers_layout.addWidget(self.t_layer, 2, 1, 1, 1)

        self.penetration_t = QLineEdit(self.Geometriadocordao)
        self.penetration_t.setObjectName(u"penetration_t")

        self.predicion_layers_layout.addWidget(self.penetration_t, 4, 3, 1, 1)

        self.layer_area = QLineEdit(self.Geometriadocordao)
        self.layer_area.setObjectName(u"layer_area")

        self.predicion_layers_layout.addWidget(self.layer_area, 3, 1, 1, 1)

        self.substrate_area = QLineEdit(self.Geometriadocordao)
        self.substrate_area.setObjectName(u"substrate_area")

        self.predicion_layers_layout.addWidget(self.substrate_area, 5, 1, 1, 1)

        self.T_layer_label = QLabel(self.Geometriadocordao)
        self.T_layer_label.setObjectName(u"T_layer_label")
        palette30 = QPalette()
        palette30.setBrush(QPalette.Active, QPalette.WindowText, brush3)
        palette30.setBrush(QPalette.Inactive, QPalette.WindowText, brush3)
        self.T_layer_label.setPalette(palette30)

        self.predicion_layers_layout.addWidget(self.T_layer_label, 2, 0, 1, 1)

        self.prediction_layers_title = QLabel(self.Geometriadocordao)
        self.prediction_layers_title.setObjectName(u"prediction_layers_title")
        palette31 = QPalette()
        brush9 = QBrush(QColor(158, 31, 34, 255))
        brush9.setStyle(Qt.SolidPattern)
        palette31.setBrush(QPalette.Active, QPalette.WindowText, brush9)
        palette31.setBrush(QPalette.Inactive, QPalette.WindowText, brush9)
        self.prediction_layers_title.setPalette(palette31)

        self.predicion_layers_layout.addWidget(self.prediction_layers_title, 0, 0, 1, 4)

        self.penetration_t_label = QLabel(self.Geometriadocordao)
        self.penetration_t_label.setObjectName(u"penetration_t_label")
        palette32 = QPalette()
        palette32.setBrush(QPalette.Active, QPalette.WindowText, brush3)
        palette32.setBrush(QPalette.Inactive, QPalette.WindowText, brush3)
        self.penetration_t_label.setPalette(palette32)

        self.predicion_layers_layout.addWidget(self.penetration_t_label, 4, 2, 1, 1)

        self.layer_area_label = QLabel(self.Geometriadocordao)
        self.layer_area_label.setObjectName(u"layer_area_label")
        palette33 = QPalette()
        palette33.setBrush(QPalette.Active, QPalette.WindowText, brush3)
        palette33.setBrush(QPalette.Inactive, QPalette.WindowText, brush3)
        self.layer_area_label.setPalette(palette33)

        self.predicion_layers_layout.addWidget(self.layer_area_label, 3, 0, 1, 1)

        self.width_t = QLineEdit(self.Geometriadocordao)
        self.width_t.setObjectName(u"width_t")

        self.predicion_layers_layout.addWidget(self.width_t, 2, 3, 1, 1)

        self.t_subtrate_label = QLabel(self.Geometriadocordao)
        self.t_subtrate_label.setObjectName(u"t_subtrate_label")
        palette34 = QPalette()
        palette34.setBrush(QPalette.Active, QPalette.WindowText, brush3)
        palette34.setBrush(QPalette.Inactive, QPalette.WindowText, brush3)
        self.t_subtrate_label.setPalette(palette34)

        self.predicion_layers_layout.addWidget(self.t_subtrate_label, 4, 0, 1, 1)

        self.verticalSpacer = QSpacerItem(0, 20, QSizePolicy.Minimum, QSizePolicy.Minimum)

        self.predicion_layers_layout.addItem(self.verticalSpacer, 1, 1, 1, 1)


        self.gridLayout_4.addLayout(self.predicion_layers_layout, 4, 5, 2, 2)

        self.electric_parameters_layout = QGridLayout()
        self.electric_parameters_layout.setObjectName(u"electric_parameters_layout")
        self.electric_parameters_layout.setHorizontalSpacing(20)
        self.electric_parameters_layout.setVerticalSpacing(5)
        self.electric_parameters_layout.setContentsMargins(-1, -1, -1, 0)
        self.ws_icon = QLabel(self.Geometriadocordao)
        self.ws_icon.setObjectName(u"ws_icon")
        sizePolicy3 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy3.setHorizontalStretch(10)
        sizePolicy3.setVerticalStretch(5)
        sizePolicy3.setHeightForWidth(self.ws_icon.sizePolicy().hasHeightForWidth())
        self.ws_icon.setSizePolicy(sizePolicy3)
        palette35 = QPalette()
        palette35.setBrush(QPalette.Active, QPalette.WindowText, brush3)
        palette35.setBrush(QPalette.Active, QPalette.Button, brush8)
        palette35.setBrush(QPalette.Active, QPalette.Base, brush8)
        palette35.setBrush(QPalette.Active, QPalette.Window, brush8)
        palette35.setBrush(QPalette.Inactive, QPalette.WindowText, brush3)
        palette35.setBrush(QPalette.Inactive, QPalette.Button, brush8)
        palette35.setBrush(QPalette.Inactive, QPalette.Base, brush8)
        palette35.setBrush(QPalette.Inactive, QPalette.Window, brush8)
        palette35.setBrush(QPalette.Disabled, QPalette.Button, brush8)
        palette35.setBrush(QPalette.Disabled, QPalette.Base, brush8)
        palette35.setBrush(QPalette.Disabled, QPalette.Window, brush8)
        self.ws_icon.setPalette(palette35)
        font7 = QFont()
        font7.setBold(True)
        font7.setItalic(True)
        self.ws_icon.setFont(font7)
        self.ws_icon.setStyleSheet(u"background-color:rgb(245, 230, 196)")

        self.electric_parameters_layout.addWidget(self.ws_icon, 2, 0, 1, 1)

        self.ts_label = QLabel(self.Geometriadocordao)
        self.ts_label.setObjectName(u"ts_label")
        palette36 = QPalette()
        palette36.setBrush(QPalette.Active, QPalette.WindowText, brush1)
        palette36.setBrush(QPalette.Active, QPalette.Button, brush6)
        brush10 = QBrush(QColor(255, 85, 0, 255))
        brush10.setStyle(Qt.SolidPattern)
        palette36.setBrush(QPalette.Active, QPalette.Light, brush10)
        palette36.setBrush(QPalette.Active, QPalette.Base, brush6)
        palette36.setBrush(QPalette.Active, QPalette.Window, brush6)
        palette36.setBrush(QPalette.Inactive, QPalette.WindowText, brush1)
        palette36.setBrush(QPalette.Inactive, QPalette.Button, brush6)
        palette36.setBrush(QPalette.Inactive, QPalette.Light, brush10)
        palette36.setBrush(QPalette.Inactive, QPalette.Base, brush6)
        palette36.setBrush(QPalette.Inactive, QPalette.Window, brush6)
        palette36.setBrush(QPalette.Disabled, QPalette.Button, brush6)
        palette36.setBrush(QPalette.Disabled, QPalette.Light, brush10)
        palette36.setBrush(QPalette.Disabled, QPalette.Base, brush6)
        palette36.setBrush(QPalette.Disabled, QPalette.Window, brush6)
        self.ts_label.setPalette(palette36)
        self.ts_label.setFont(font)
        self.ts_label.setStyleSheet(u"background-color:rgb(245, 132, 153)")
        self.ts_label.setAlignment(Qt.AlignCenter)

        self.electric_parameters_layout.addWidget(self.ts_label, 5, 1, 1, 1)

        self.ws_input1 = QLineEdit(self.Geometriadocordao)
        self.ws_input1.setObjectName(u"ws_input1")
        
        sizePolicy5 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        sizePolicy5.setHorizontalStretch(0)
        sizePolicy5.setVerticalStretch(0)
        sizePolicy5.setHeightForWidth(self.ws_input1.sizePolicy().hasHeightForWidth())
        self.ws_input1.setSizePolicy(sizePolicy5)

        self.ws_input2 = QLineEdit(self.Geometriadocordao)
        self.ws_input2.setObjectName(u"ws_input2")
        self.electric_parameters_layout.addWidget(self.ws_input2, 3, 1, 1, 1)

        
        self.ws_input1.returnPressed.connect(lambda: self.ws_input2.setText(self.SpeedMeasureConverter(self.ws_input1.text(), 1)))

        
        self.ws_input2.editingFinished.connect(lambda: self.ws_input1.setText(self.SpeedMeasureConverter(self.ws_input2.text(), -1)))


        self.v_label = QLabel(self.Geometriadocordao)
        self.v_label.setObjectName(u"v_label")
        palette37 = QPalette()
        palette37.setBrush(QPalette.Active, QPalette.WindowText, brush1)
        palette37.setBrush(QPalette.Active, QPalette.Button, brush6)
        palette37.setBrush(QPalette.Active, QPalette.Light, brush10)
        palette37.setBrush(QPalette.Active, QPalette.Base, brush6)
        palette37.setBrush(QPalette.Active, QPalette.Window, brush6)
        palette37.setBrush(QPalette.Inactive, QPalette.WindowText, brush1)
        palette37.setBrush(QPalette.Inactive, QPalette.Button, brush6)
        palette37.setBrush(QPalette.Inactive, QPalette.Light, brush10)
        palette37.setBrush(QPalette.Inactive, QPalette.Base, brush6)
        palette37.setBrush(QPalette.Inactive, QPalette.Window, brush6)
        palette37.setBrush(QPalette.Disabled, QPalette.Button, brush6)
        palette37.setBrush(QPalette.Disabled, QPalette.Light, brush10)
        palette37.setBrush(QPalette.Disabled, QPalette.Base, brush6)
        palette37.setBrush(QPalette.Disabled, QPalette.Window, brush6)
        self.v_label.setPalette(palette37)
        self.v_label.setFont(font)
        self.v_label.setStyleSheet(u"background-color:rgb(245, 132, 153)")
        self.v_label.setAlignment(Qt.AlignCenter)

        self.electric_parameters_layout.addWidget(self.v_label, 9, 1, 1, 1)

        self.ts_icon = QLabel(self.Geometriadocordao)
        self.ts_icon.setObjectName(u"ts_icon")
        sizePolicy1.setHeightForWidth(self.ts_icon.sizePolicy().hasHeightForWidth())
        self.ts_icon.setSizePolicy(sizePolicy1)
        palette38 = QPalette()
        palette38.setBrush(QPalette.Active, QPalette.WindowText, brush3)
        palette38.setBrush(QPalette.Active, QPalette.Button, brush8)
        palette38.setBrush(QPalette.Active, QPalette.Base, brush8)
        palette38.setBrush(QPalette.Active, QPalette.Window, brush8)
        palette38.setBrush(QPalette.Inactive, QPalette.WindowText, brush3)
        palette38.setBrush(QPalette.Inactive, QPalette.Button, brush8)
        palette38.setBrush(QPalette.Inactive, QPalette.Base, brush8)
        palette38.setBrush(QPalette.Inactive, QPalette.Window, brush8)
        palette38.setBrush(QPalette.Disabled, QPalette.Button, brush8)
        palette38.setBrush(QPalette.Disabled, QPalette.Base, brush8)
        palette38.setBrush(QPalette.Disabled, QPalette.Window, brush8)
        self.ts_icon.setPalette(palette38)
        self.ts_icon.setFont(font7)
        self.ts_icon.setStyleSheet(u"background-color:rgb(245, 230, 196)")

        self.electric_parameters_layout.addWidget(self.ts_icon, 5, 0, 1, 1)

        self.v_icon = QLabel(self.Geometriadocordao)
        self.v_icon.setObjectName(u"v_icon")
        sizePolicy1.setHeightForWidth(self.v_icon.sizePolicy().hasHeightForWidth())
        self.v_icon.setSizePolicy(sizePolicy1)
        palette39 = QPalette()
        palette39.setBrush(QPalette.Active, QPalette.WindowText, brush3)
        palette39.setBrush(QPalette.Active, QPalette.Button, brush8)
        palette39.setBrush(QPalette.Active, QPalette.Base, brush8)
        palette39.setBrush(QPalette.Active, QPalette.Window, brush8)
        palette39.setBrush(QPalette.Inactive, QPalette.WindowText, brush3)
        palette39.setBrush(QPalette.Inactive, QPalette.Button, brush8)
        palette39.setBrush(QPalette.Inactive, QPalette.Base, brush8)
        palette39.setBrush(QPalette.Inactive, QPalette.Window, brush8)
        palette39.setBrush(QPalette.Disabled, QPalette.Button, brush8)
        palette39.setBrush(QPalette.Disabled, QPalette.Base, brush8)
        palette39.setBrush(QPalette.Disabled, QPalette.Window, brush8)
        self.v_icon.setPalette(palette39)
        self.v_icon.setFont(font7)
        self.v_icon.setStyleSheet(u"background-color:rgb(245, 230, 196)")

        self.electric_parameters_layout.addWidget(self.v_icon, 9, 0, 1, 1)

        self.ws_label = QLabel(self.Geometriadocordao)
        self.ws_label.setObjectName(u"ws_label")
        sizePolicy4 = QSizePolicy(QSizePolicy.MinimumExpanding, QSizePolicy.Fixed)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.ws_label.sizePolicy().hasHeightForWidth())
        self.ws_label.setSizePolicy(sizePolicy4)
        self.ws_label.setMinimumSize(QSize(87, 0))
        palette40 = QPalette()
        palette40.setBrush(QPalette.Active, QPalette.WindowText, brush1)
        palette40.setBrush(QPalette.Active, QPalette.Button, brush6)
        palette40.setBrush(QPalette.Active, QPalette.Light, brush10)
        palette40.setBrush(QPalette.Active, QPalette.Base, brush6)
        palette40.setBrush(QPalette.Active, QPalette.Window, brush6)
        palette40.setBrush(QPalette.Inactive, QPalette.WindowText, brush1)
        palette40.setBrush(QPalette.Inactive, QPalette.Button, brush6)
        palette40.setBrush(QPalette.Inactive, QPalette.Light, brush10)
        palette40.setBrush(QPalette.Inactive, QPalette.Base, brush6)
        palette40.setBrush(QPalette.Inactive, QPalette.Window, brush6)
        palette40.setBrush(QPalette.Disabled, QPalette.Button, brush6)
        palette40.setBrush(QPalette.Disabled, QPalette.Light, brush10)
        palette40.setBrush(QPalette.Disabled, QPalette.Base, brush6)
        palette40.setBrush(QPalette.Disabled, QPalette.Window, brush6)
        self.ws_label.setPalette(palette40)
        font8 = QFont()
        font8.setPointSize(8)
        font8.setBold(True)
        self.ws_label.setFont(font8)
        self.ws_label.setStyleSheet(u"background-color:rgb(245, 132, 153)")
        self.ws_label.setAlignment(Qt.AlignCenter)

        self.electric_parameters_layout.addWidget(self.ws_label, 1, 1, 1, 1)

        self.ts_input1 = QLineEdit(self.Geometriadocordao)
        self.ts_input1.setObjectName(u"ts_input1")



        self.electric_parameters_layout.addWidget(self.ts_input1, 6, 1, 1, 1)

        self.ts_input1.editingFinished.connect(lambda: self.ts_input2.setText(self.SpeedMeasureConverter(self.ts_input1.text(), 1)))


        self.ts_input2 = QLineEdit(self.Geometriadocordao)
        self.ts_input2.setObjectName(u"ts_input2")

        self.electric_parameters_layout.addWidget(self.ts_input2, 7, 1, 1, 1)

        self.ts_input2.editingFinished.connect(lambda: self.ts_input1.setText(self.SpeedMeasureConverter(self.ts_input2.text(), -1)))
        self.v_input = QLineEdit(self.Geometriadocordao)
        self.v_input.setObjectName(u"v_input")

        self.electric_parameters_layout.addWidget(self.v_input, 10, 1, 1, 1)

        self.ws_measure1 = QLabel(self.Geometriadocordao)
        self.ws_measure1.setObjectName(u"ws_measure1")
        palette41 = QPalette()
        palette41.setBrush(QPalette.Active, QPalette.WindowText, brush3)
        palette41.setBrush(QPalette.Inactive, QPalette.WindowText, brush3)
        self.ws_measure1.setPalette(palette41)

        self.electric_parameters_layout.addWidget(self.ws_measure1, 2, 2, 1, 1)

        self.ts_measure1 = QLabel(self.Geometriadocordao)
        self.ts_measure1.setObjectName(u"ts_measure1")
        palette42 = QPalette()
        palette42.setBrush(QPalette.Active, QPalette.WindowText, brush3)
        palette42.setBrush(QPalette.Inactive, QPalette.WindowText, brush3)
        self.ts_measure1.setPalette(palette42)

        self.electric_parameters_layout.addWidget(self.ts_measure1, 6, 2, 1, 1)

        self.verticalSpacer_7 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Minimum)

        self.electric_parameters_layout.addItem(self.verticalSpacer_7, 8, 1, 1, 1)


        self.verticalSpacer_6 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Minimum)

        self.electric_parameters_layout.addItem(self.verticalSpacer_6, 4, 1, 1, 1)

        
        self.electric_parameters_layout.addWidget(self.ws_input1, 2, 1, 1, 1)

        self.ts_measure2 = QLabel(self.Geometriadocordao)
        self.ts_measure2.setObjectName(u"ts_measure2")
        palette43 = QPalette()
        palette43.setBrush(QPalette.Active, QPalette.WindowText, brush3)
        palette43.setBrush(QPalette.Inactive, QPalette.WindowText, brush3)
        self.ts_measure2.setPalette(palette43)

        self.electric_parameters_layout.addWidget(self.ts_measure2, 7, 2, 1, 1)

        self.v_measure = QLabel(self.Geometriadocordao)
        self.v_measure.setObjectName(u"v_measure")
        palette44 = QPalette()
        palette44.setBrush(QPalette.Active, QPalette.WindowText, brush3)
        palette44.setBrush(QPalette.Inactive, QPalette.WindowText, brush3)
        self.v_measure.setPalette(palette44)
        self.v_measure.raise_()

        self.electric_parameters_layout.addWidget(self.v_measure, 10, 2, 1, 1)

        self.ws_measure2 = QLabel(self.Geometriadocordao)
        self.ws_measure2.setObjectName(u"ws_measure2")
        palette45 = QPalette()
        palette45.setBrush(QPalette.Active, QPalette.WindowText, brush3)
        palette45.setBrush(QPalette.Inactive, QPalette.WindowText, brush3)
        self.ws_measure2.setPalette(palette45)

        self.electric_parameters_layout.addWidget(self.ws_measure2, 3, 2, 1, 1)


        self.gridLayout_4.addLayout(self.electric_parameters_layout, 1, 1, 2, 1)

        self.wire_characteristics_layout = QGridLayout()
        self.wire_characteristics_layout.setSpacing(20)
        self.wire_characteristics_layout.setObjectName(u"wire_characteristics_layout")
        self.wire_characteristics_layout.setContentsMargins(10, -1, 20, 10)
        self.diameter_label = QLabel(self.Geometriadocordao)
        self.diameter_label.setObjectName(u"diameter_label")
        self.diameter_label.setEnabled(True)
        self.diameter_label.setMinimumSize(QSize(50, 0))
        palette46 = QPalette()
        palette46.setBrush(QPalette.Active, QPalette.WindowText, brush3)
        palette46.setBrush(QPalette.Active, QPalette.Button, brush8)
        palette46.setBrush(QPalette.Active, QPalette.Base, brush8)
        palette46.setBrush(QPalette.Active, QPalette.Window, brush8)
        palette46.setBrush(QPalette.Inactive, QPalette.WindowText, brush3)
        palette46.setBrush(QPalette.Inactive, QPalette.Button, brush8)
        palette46.setBrush(QPalette.Inactive, QPalette.Base, brush8)
        palette46.setBrush(QPalette.Inactive, QPalette.Window, brush8)
        palette46.setBrush(QPalette.Disabled, QPalette.Button, brush8)
        palette46.setBrush(QPalette.Disabled, QPalette.Base, brush8)
        palette46.setBrush(QPalette.Disabled, QPalette.Window, brush8)
        self.diameter_label.setPalette(palette46)
        self.diameter_label.setFont(font8)
        self.diameter_label.setStyleSheet(u"background-color:rgb(245, 230, 196)")
        self.diameter_label.setAlignment(Qt.AlignCenter)

        self.wire_characteristics_layout.addWidget(self.diameter_label, 1, 0, 1, 1)

        self.wire_characteristics_title = QLabel(self.Geometriadocordao)
        self.wire_characteristics_title.setObjectName(u"wire_characteristics_title")
        palette47 = QPalette()
        palette47.setBrush(QPalette.Active, QPalette.WindowText, brush9)
        palette47.setBrush(QPalette.Inactive, QPalette.WindowText, brush9)
        self.wire_characteristics_title.setPalette(palette47)
        self.wire_characteristics_title.setStyleSheet(u"")
        self.wire_characteristics_title.setAlignment(Qt.AlignBottom|Qt.AlignHCenter)

        self.wire_characteristics_layout.addWidget(self.wire_characteristics_title, 0, 0, 1, 3)

        self.diameter = QLineEdit(self.Geometriadocordao)
        self.diameter.setObjectName(u"diameter")

        self.wire_characteristics_layout.addWidget(self.diameter, 1, 1, 1, 1)

        self.diameter_measure = QLabel(self.Geometriadocordao)
        self.diameter_measure.setObjectName(u"diameter_measure")
        palette48 = QPalette()
        palette48.setBrush(QPalette.Active, QPalette.WindowText, brush3)
        palette48.setBrush(QPalette.Inactive, QPalette.WindowText, brush3)
        self.diameter_measure.setPalette(palette48)

        self.wire_characteristics_layout.addWidget(self.diameter_measure, 1, 2, 1, 1)


        self.gridLayout_4.addLayout(self.wire_characteristics_layout, 3, 5, 1, 1)

        self.horizontalSpacer = QSpacerItem(100, 20, QSizePolicy.Minimum, QSizePolicy.Minimum)

        self.gridLayout_4.addItem(self.horizontalSpacer, 2, 4, 1, 1)

        self.geometric_prediction_layout = QGridLayout()
        self.geometric_prediction_layout.setObjectName(u"geometric_prediction_layout")
        self.geometric_prediction_layout.setHorizontalSpacing(10)
        self.geometric_prediction_layout.setVerticalSpacing(20)
        self.geometric_prediction_layout.setContentsMargins(10, -1, 10, 10)
        self.zta_label = QLabel(self.Geometriadocordao)
        self.zta_label.setObjectName(u"zta_label")
        palette49 = QPalette()
        palette49.setBrush(QPalette.Active, QPalette.WindowText, brush3)
        palette49.setBrush(QPalette.Inactive, QPalette.WindowText, brush3)
        self.zta_label.setPalette(palette49)
        self.zta_label.setAlignment(Qt.AlignCenter)

        self.geometric_prediction_layout.addWidget(self.zta_label, 6, 0, 1, 1)

        self.penetration_label = QLabel(self.Geometriadocordao)
        self.penetration_label.setObjectName(u"penetration_label")
        palette50 = QPalette()
        palette50.setBrush(QPalette.Active, QPalette.WindowText, brush3)
        palette50.setBrush(QPalette.Inactive, QPalette.WindowText, brush3)
        self.penetration_label.setPalette(palette50)
        self.penetration_label.setAlignment(Qt.AlignCenter)

        self.geometric_prediction_layout.addWidget(self.penetration_label, 5, 0, 1, 1)

        self.zta_measure = QLabel(self.Geometriadocordao)
        self.zta_measure.setObjectName(u"zta_measure")
        palette51 = QPalette()
        palette51.setBrush(QPalette.Active, QPalette.WindowText, brush3)
        palette51.setBrush(QPalette.Inactive, QPalette.WindowText, brush3)
        self.zta_measure.setPalette(palette51)

        self.geometric_prediction_layout.addWidget(self.zta_measure, 6, 3, 1, 1)

        self.height_label = QLabel(self.Geometriadocordao)
        self.height_label.setObjectName(u"height_label")
        palette52 = QPalette()
        palette52.setBrush(QPalette.Active, QPalette.WindowText, brush3)
        palette52.setBrush(QPalette.Inactive, QPalette.WindowText, brush3)
        self.height_label.setPalette(palette52)
        self.height_label.setAlignment(Qt.AlignCenter)

        self.geometric_prediction_layout.addWidget(self.height_label, 4, 0, 1, 1)

        self.penetration = QLineEdit(self.Geometriadocordao)
        self.penetration.setObjectName(u"penetration")

        self.geometric_prediction_layout.addWidget(self.penetration, 5, 1, 1, 2)

        self.zta = QLineEdit(self.Geometriadocordao)
        self.zta.setObjectName(u"zta")

        self.geometric_prediction_layout.addWidget(self.zta, 6, 1, 1, 2)

        self.t_solid_label = QLabel(self.Geometriadocordao)
        self.t_solid_label.setObjectName(u"t_solid_label")
        palette53 = QPalette()
        palette53.setBrush(QPalette.Active, QPalette.WindowText, brush3)
        palette53.setBrush(QPalette.Inactive, QPalette.WindowText, brush3)
        self.t_solid_label.setPalette(palette53)
        self.t_solid_label.setAlignment(Qt.AlignCenter)

        self.geometric_prediction_layout.addWidget(self.t_solid_label, 7, 0, 1, 1)

        self.t_solid_measure = QLabel(self.Geometriadocordao)
        self.t_solid_measure.setObjectName(u"t_solid_measure")
        palette54 = QPalette()
        palette54.setBrush(QPalette.Active, QPalette.WindowText, brush3)
        palette54.setBrush(QPalette.Inactive, QPalette.WindowText, brush3)
        self.t_solid_measure.setPalette(palette54)

        self.geometric_prediction_layout.addWidget(self.t_solid_measure, 7, 3, 1, 1)

        self.calculate_button = QPushButton(self.Geometriadocordao)
        self.calculate_button.setObjectName(u"calculate_button")
        sizePolicy2.setHeightForWidth(self.calculate_button.sizePolicy().hasHeightForWidth())
        self.calculate_button.setSizePolicy(sizePolicy2)
        self.calculate_button.setMinimumSize(QSize(0, 20))
        palette55 = QPalette()
        palette55.setBrush(QPalette.Active, QPalette.WindowText, brush9)
        palette55.setBrush(QPalette.Active, QPalette.ButtonText, brush9)
        palette55.setBrush(QPalette.Inactive, QPalette.WindowText, brush9)
        palette55.setBrush(QPalette.Inactive, QPalette.ButtonText, brush9)
        self.calculate_button.setPalette(palette55)

        self.geometric_prediction_layout.addWidget(self.calculate_button, 1, 1, 1, 2)

        self.calculate_button.clicked.connect(lambda: self.GeometricPredictionCallback(float(self.ws_input1.text()), float(self.ts_input1.text()), float(self.v_input.text()), 
                                                                                       float(self.I.text()), float(self.melting_point.text()), 
                                                                                       float(self.specific_heat.text()), float(self.viscosity.text()), float(self.density.text()), 
                                                                                       float(self.thermal_conductivity.text()), float(self.diameter.text())))

        self.penetration_measure = QLabel(self.Geometriadocordao)
        self.penetration_measure.setObjectName(u"penetration_measure")
        palette56 = QPalette()
        palette56.setBrush(QPalette.Active, QPalette.WindowText, brush3)
        palette56.setBrush(QPalette.Inactive, QPalette.WindowText, brush3)
        self.penetration_measure.setPalette(palette56)

        self.geometric_prediction_layout.addWidget(self.penetration_measure, 5, 3, 1, 1)

        self.width = QLineEdit(self.Geometriadocordao)
        self.width.setObjectName(u"width")
        sizePolicy6 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.MinimumExpanding)
        sizePolicy6.setHorizontalStretch(0)
        sizePolicy6.setVerticalStretch(0)
        sizePolicy6.setHeightForWidth(self.width.sizePolicy().hasHeightForWidth())
        self.width.setSizePolicy(sizePolicy6)
        self.width.setMinimumSize(QSize(0, 22))

        self.geometric_prediction_layout.addWidget(self.width, 3, 1, 1, 2)

        self.width_label = QLabel(self.Geometriadocordao)
        self.width_label.setObjectName(u"width_label")
        palette57 = QPalette()
        palette57.setBrush(QPalette.Active, QPalette.WindowText, brush3)
        palette57.setBrush(QPalette.Inactive, QPalette.WindowText, brush3)
        self.width_label.setPalette(palette57)
        self.width_label.setAlignment(Qt.AlignCenter)

        self.geometric_prediction_layout.addWidget(self.width_label, 3, 0, 1, 1)

        self.width_measure = QLabel(self.Geometriadocordao)
        self.width_measure.setObjectName(u"width_measure")
        palette58 = QPalette()
        palette58.setBrush(QPalette.Active, QPalette.WindowText, brush3)
        palette58.setBrush(QPalette.Inactive, QPalette.WindowText, brush3)
        self.width_measure.setPalette(palette58)

        self.geometric_prediction_layout.addWidget(self.width_measure, 3, 3, 1, 1)

        self.height_measure = QLabel(self.Geometriadocordao)
        self.height_measure.setObjectName(u"height_measure")
        palette59 = QPalette()
        palette59.setBrush(QPalette.Active, QPalette.WindowText, brush3)
        palette59.setBrush(QPalette.Inactive, QPalette.WindowText, brush3)
        self.height_measure.setPalette(palette59)

        self.geometric_prediction_layout.addWidget(self.height_measure, 4, 3, 1, 1)

        self.geometric_prediction_title = QLabel(self.Geometriadocordao)
        self.geometric_prediction_title.setObjectName(u"geometric_prediction_title")
        palette60 = QPalette()
        palette60.setBrush(QPalette.Active, QPalette.WindowText, brush9)
        palette60.setBrush(QPalette.Inactive, QPalette.WindowText, brush9)
        self.geometric_prediction_title.setPalette(palette60)
        font9 = QFont()
        font9.setKerning(True)
        self.geometric_prediction_title.setFont(font9)
        self.geometric_prediction_title.setLayoutDirection(Qt.LeftToRight)
        self.geometric_prediction_title.setAlignment(Qt.AlignCenter)

        self.geometric_prediction_layout.addWidget(self.geometric_prediction_title, 0, 0, 1, 4)

        self.t_solid = QLineEdit(self.Geometriadocordao)
        self.t_solid.setObjectName(u"t_solid")

        self.geometric_prediction_layout.addWidget(self.t_solid, 7, 1, 1, 2)

        self.height = QLineEdit(self.Geometriadocordao)
        self.height.setObjectName(u"height")

        self.geometric_prediction_layout.addWidget(self.height, 4, 1, 1, 2)

        self.gp_spacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.geometric_prediction_layout.addItem(self.gp_spacer, 2, 1, 1, 1)


        self.gridLayout_4.addLayout(self.geometric_prediction_layout, 1, 6, 3, 1)

        self.dial_layout = QVBoxLayout()
        self.dial_layout.setObjectName(u"dial_layout")
        self.dial_layout.setContentsMargins(-1, -1, -1, 10)
        self.ws_dial = QDial(self.Geometriadocordao)
        self.ws_dial.setObjectName(u"ws_dial")

        self.dial_layout.addWidget(self.ws_dial)

        self.ts_dial = QDial(self.Geometriadocordao)
        self.ts_dial.setObjectName(u"ts_dial")

        self.dial_layout.addWidget(self.ts_dial)

        self.v_dial = QDial(self.Geometriadocordao)
        self.v_dial.setObjectName(u"v_dial")

        self.dial_layout.addWidget(self.v_dial)


        self.gridLayout_4.addLayout(self.dial_layout, 1, 0, 2, 1)

        self.ElectricParameters_title = QLabel(self.Geometriadocordao)
        self.ElectricParameters_title.setObjectName(u"ElectricParameters_title")
        sizePolicy7 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Minimum)
        sizePolicy7.setHorizontalStretch(0)
        sizePolicy7.setVerticalStretch(0)
        sizePolicy7.setHeightForWidth(self.ElectricParameters_title.sizePolicy().hasHeightForWidth())
        self.ElectricParameters_title.setSizePolicy(sizePolicy7)
        palette61 = QPalette()
        palette61.setBrush(QPalette.Active, QPalette.WindowText, brush7)
        palette61.setBrush(QPalette.Inactive, QPalette.WindowText, brush7)
        self.ElectricParameters_title.setPalette(palette61)
        self.ElectricParameters_title.setFont(font)

        self.gridLayout_4.addWidget(self.ElectricParameters_title, 0, 0, 1, 2)


        self.PredictionSubTabWidget.addTab(self.Geometriadocordao, "")
        
        self.ElectricParameters_title.raise_()
        self.altura = QWidget()
        self.altura.setObjectName(u"altura")
        palette62 = QPalette()
        brush11 = QBrush(QColor(240, 222, 200, 255))
        brush11.setStyle(Qt.SolidPattern)
        palette62.setBrush(QPalette.Active, QPalette.Button, brush11)
        palette62.setBrush(QPalette.Active, QPalette.Base, brush11)
        palette62.setBrush(QPalette.Active, QPalette.Window, brush11)
        palette62.setBrush(QPalette.Inactive, QPalette.Button, brush11)
        palette62.setBrush(QPalette.Inactive, QPalette.Base, brush11)
        palette62.setBrush(QPalette.Inactive, QPalette.Window, brush11)
        palette62.setBrush(QPalette.Disabled, QPalette.Button, brush11)
        palette62.setBrush(QPalette.Disabled, QPalette.Base, brush11)
        palette62.setBrush(QPalette.Disabled, QPalette.Window, brush11)
        self.altura.setPalette(palette62)
        self.altura.setStyleSheet(u"#altura{\n"
"	background-color: rgb(240, 222, 200);\n"
"}")
        self.verticalLayout = QVBoxLayout(self.altura)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.PredictionSubTabWidget.addTab(self.altura, "")
        self.redes_neurais_geometria = QWidget()
        self.redes_neurais_geometria.setObjectName(u"redes_neurais_geometria")
        self.test_label = QLabel(self.redes_neurais_geometria)
        self.test_label.setObjectName(u"test_label")
        self.test_label.setGeometry(QRect(320, 60, 49, 16))
        self.PredictionSubTabWidget.addTab(self.redes_neurais_geometria, "")
        self.balanco_fase = QWidget()
        self.balanco_fase.setObjectName(u"balanco_fase")
        self.PredictionSubTabWidget.addTab(self.balanco_fase, "")
        self.distancia_interdendritica = QWidget()
        self.distancia_interdendritica.setObjectName(u"distancia_interdendritica")
        self.PredictionSubTabWidget.addTab(self.distancia_interdendritica, "")
        self.tamanho_grao = QWidget()
        self.tamanho_grao.setObjectName(u"tamanho_grao")
        self.PredictionSubTabWidget.addTab(self.tamanho_grao, "")

        self.verticalLayout_3.addWidget(self.PredictionSubTabWidget)

        self.primaryTabWidget.addTab(self.PredictionWidget, "")
        self.MeasureToolWidget = QWidget()
        self.MeasureToolWidget.setObjectName(u"MeasureToolWidget")
        self.MeasureToolSubTabWidget = QTabWidget(self.MeasureToolWidget)
        self.MeasureToolSubTabWidget.setObjectName(u"MeasureToolSubTabWidget")
        self.MeasureToolSubTabWidget.setGeometry(QRect(0, 0, 800, 570))
        palette63 = QPalette()
        brush12 = QBrush(QColor(85, 170, 0, 255))
        brush12.setStyle(Qt.SolidPattern)
        palette63.setBrush(QPalette.Active, QPalette.WindowText, brush12)
        palette63.setBrush(QPalette.Inactive, QPalette.WindowText, brush12)
        self.MeasureToolSubTabWidget.setPalette(palette63)
        self.melting_pool = QWidget()
        self.melting_pool.setObjectName(u"melting_pool")
        palette64 = QPalette()
        brush13 = QBrush(QColor(240, 150, 150, 255))
        brush13.setStyle(Qt.SolidPattern)
        palette64.setBrush(QPalette.Active, QPalette.Button, brush13)
        palette64.setBrush(QPalette.Active, QPalette.Base, brush13)
        palette64.setBrush(QPalette.Active, QPalette.Window, brush13)
        palette64.setBrush(QPalette.Inactive, QPalette.Button, brush13)
        palette64.setBrush(QPalette.Inactive, QPalette.Base, brush13)
        palette64.setBrush(QPalette.Inactive, QPalette.Window, brush13)
        palette64.setBrush(QPalette.Disabled, QPalette.Button, brush13)
        palette64.setBrush(QPalette.Disabled, QPalette.Base, brush13)
        palette64.setBrush(QPalette.Disabled, QPalette.Window, brush13)
        self.melting_pool.setPalette(palette64)
        self.melting_pool.setStyleSheet(u"#melting_pool{\n"
"	background-color: rgb(240, 150, 150);\n"
"\n"
"}")
        self.MeasureToolSubTabWidget.addTab(self.melting_pool, "")
        self.bead_geometry = QWidget()
        self.bead_geometry.setObjectName(u"bead_geometry")
        palette65 = QPalette()
        brush14 = QBrush(QColor(232, 181, 146, 255))
        brush14.setStyle(Qt.SolidPattern)
        palette65.setBrush(QPalette.Active, QPalette.Window, brush14)
        palette65.setBrush(QPalette.Inactive, QPalette.Window, brush14)
        palette65.setBrush(QPalette.Disabled, QPalette.Base, brush14)
        palette65.setBrush(QPalette.Disabled, QPalette.Window, brush14)
        self.bead_geometry.setPalette(palette65)
        self.MeasureToolSubTabWidget.addTab(self.bead_geometry, "")
        self.primaryTabWidget.addTab(self.MeasureToolWidget, "")
        self.tab_3 = QWidget()
        self.tab_3.setObjectName(u"tab_3")
        self.primaryTabWidget.addTab(self.tab_3, "")
        self.tab_4 = QWidget()
        self.tab_4.setObjectName(u"tab_4")
        self.primaryTabWidget.addTab(self.tab_4, "")
        self.tab_5 = QWidget()
        self.tab_5.setObjectName(u"tab_5")
        self.primaryTabWidget.addTab(self.tab_5, "")
        self.tab_6 = QWidget()
        self.tab_6.setObjectName(u"tab_6")
        self.primaryTabWidget.addTab(self.tab_6, "")
        AMS_Interface.setCentralWidget(self.centralwidget)

        self.retranslateUi(AMS_Interface)

        self.primaryTabWidget.setCurrentIndex(0)
        self.PredictionSubTabWidget.setCurrentIndex(2)
        self.MeasureToolSubTabWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(AMS_Interface)



        # Default Parameters: Common Steel

        mp_default = 1450   # Melting Point
        sh_default = 0.11   # Specific Heat
        vi_default = 0.003  # Viscosity
        de_default = 7.89   # Density
        ct_default = 71.5   # Thermal Conductivity
        em_default = 0.75   # Emissivity

        self.melting_point.setText(str(mp_default))
        self.specific_heat.setText(str(sh_default))
        self.viscosity.setText(str(vi_default))
        self.density.setText(str(de_default))
        self.thermal_conductivity.setText(str(ct_default))
        self.emissivity.setText(str(em_default))

        # Default Parameters: Análise de dados.xlsx (linha 1)

        self.ws_input2.setText("3")
        self.ts_input1.setText("8.33")
        self.v_input.setText("17.1")
        self.I.setText("83")
        self.diameter.setText("1.2")
        # ///////////////////////////////////////////////////
        
    # setupUi

    def retranslateUi(self, AMS_Interface):
        AMS_Interface.setWindowTitle(QCoreApplication.translate("AMS_Interface", u"MainWindow", None))
        self.current_label.setText(QCoreApplication.translate("AMS_Interface", u"Current", None))
        self.current_title.setText(QCoreApplication.translate("AMS_Interface", u"Electric Current", None))
        self.melting_point_label_2.setText(QCoreApplication.translate("AMS_Interface", u"(\u00b0C)", None))
        self.specific_heat_label_2.setText(QCoreApplication.translate("AMS_Interface", u"(cal/g. \u00b0C)", None))
        self.density_measure.setText(QCoreApplication.translate("AMS_Interface", u"(g/cm^3)", None))
        self.viscosity_label.setText(QCoreApplication.translate("AMS_Interface", u"Viscosity", None))
        self.conductivity_label_2.setText(QCoreApplication.translate("AMS_Interface", u"Ct", None))
        self.viscosity_icon.setText(QCoreApplication.translate("AMS_Interface", u"Vi", None))
        self.conductivity_label.setText(QCoreApplication.translate("AMS_Interface", u"Thermal Conductivity", None))
        self.density_label.setText(QCoreApplication.translate("AMS_Interface", u"Density", None))
        self.specific_heat_label.setText(QCoreApplication.translate("AMS_Interface", u"Specific Heat", None))
        self.emissivity_label.setText(QCoreApplication.translate("AMS_Interface", u"Emissivity", None))
        self.emissivity_icon.setText(QCoreApplication.translate("AMS_Interface", u"Em", None))
        self.melting_point_label.setText(QCoreApplication.translate("AMS_Interface", u"Melting Point", None))
        self.I_measure.setText(QCoreApplication.translate("AMS_Interface", u"(A)", None))
        self.specific_heat_icon.setText(QCoreApplication.translate("AMS_Interface", u"Ce", None))
        self.conductivity_measure.setText(QCoreApplication.translate("AMS_Interface", u"(W/(m. \u00b0K)", None))
        self.melting_point_icon.setText(QCoreApplication.translate("AMS_Interface", u"Pf", None))
        self.Fronius_checkbox.setText(QCoreApplication.translate("AMS_Interface", u"Fronius", None))
        self.density_icon.setText(QCoreApplication.translate("AMS_Interface", u"De", None))
        self.Physical_Properties_title.setText(QCoreApplication.translate("AMS_Interface", u"Physical properties", None))
        self.zta_t_label.setText(QCoreApplication.translate("AMS_Interface", u"ZTA_T\u00ba", None))
        self.Width_T_label.setText(QCoreApplication.translate("AMS_Interface", u"Width_T\u00b0", None))
        self.height_t_label.setText(QCoreApplication.translate("AMS_Interface", u"Height_T\u00b0", None))
        self.substrate_l.setText(QCoreApplication.translate("AMS_Interface", u"Substrate Area", None))
        self.T_layer_label.setText(QCoreApplication.translate("AMS_Interface", u"T\u00b0 Layer", None))
        self.prediction_layers_title.setText(QCoreApplication.translate("AMS_Interface", u"       Geometric Prediction in layers with diferent temperatures", None))
        self.penetration_t_label.setText(QCoreApplication.translate("AMS_Interface", u"Penetration_T\u00b0", None))
        self.layer_area_label.setText(QCoreApplication.translate("AMS_Interface", u"Layer Area", None))
        self.t_subtrate_label.setText(QCoreApplication.translate("AMS_Interface", u"T Substrate", None))
        self.ws_icon.setText(QCoreApplication.translate("AMS_Interface", u"Ws", None))
        self.ts_label.setText(QCoreApplication.translate("AMS_Interface", u"Travel Speed", None))
        self.v_label.setText(QCoreApplication.translate("AMS_Interface", u"Voltage", None))
        self.ts_icon.setText(QCoreApplication.translate("AMS_Interface", u"Ts", None))
        self.v_icon.setText(QCoreApplication.translate("AMS_Interface", u"V", None))
        self.ws_label.setText(QCoreApplication.translate("AMS_Interface", u"Wire Feed Speed", None))
        self.ws_measure1.setText(QCoreApplication.translate("AMS_Interface", u"(mm/s)", None))
        self.ts_measure1.setText(QCoreApplication.translate("AMS_Interface", u"(mm/s)", None))
        self.ts_measure2.setText(QCoreApplication.translate("AMS_Interface", u"(m/min)", None))
        self.v_measure.setText(QCoreApplication.translate("AMS_Interface", u"(V)", None))
        self.ws_measure2.setText(QCoreApplication.translate("AMS_Interface", u"(m/min)", None))
        self.diameter_label.setText(QCoreApplication.translate("AMS_Interface", u"Diameter", None))
        self.wire_characteristics_title.setText(QCoreApplication.translate("AMS_Interface", u"Wire Characteristics", None))
        self.diameter_measure.setText(QCoreApplication.translate("AMS_Interface", u"(mm)", None))
        self.zta_label.setText(QCoreApplication.translate("AMS_Interface", u"ZTA", None))
        self.penetration_label.setText(QCoreApplication.translate("AMS_Interface", u"Penetration", None))
        self.zta_measure.setText(QCoreApplication.translate("AMS_Interface", u"(mm)", None))
        self.height_label.setText(QCoreApplication.translate("AMS_Interface", u"Height", None))
        self.t_solid_label.setText(QCoreApplication.translate("AMS_Interface", u"tempo_solid", None))
        self.t_solid_measure.setText(QCoreApplication.translate("AMS_Interface", u"(s)", None))
        self.calculate_button.setText(QCoreApplication.translate("AMS_Interface", u"Calculate", None))
        self.penetration_measure.setText(QCoreApplication.translate("AMS_Interface", u"(mm)", None))
        self.width_label.setText(QCoreApplication.translate("AMS_Interface", u"Width", None))
        self.width_measure.setText(QCoreApplication.translate("AMS_Interface", u"(mm)", None))
        self.height_measure.setText(QCoreApplication.translate("AMS_Interface", u"(mm)", None))
        self.geometric_prediction_title.setText(QCoreApplication.translate("AMS_Interface", u"Geometric Prediction", None))
        self.ElectricParameters_title.setText(QCoreApplication.translate("AMS_Interface", u"Electric Parameters", None))
        self.rectEP.setText("")
        self.rectEC.setText("")
        self.PredictionSubTabWidget.setTabText(self.PredictionSubTabWidget.indexOf(self.Geometriadocordao), QCoreApplication.translate("AMS_Interface", u"Geometria do cord\u00e3o", None))
        self.PredictionSubTabWidget.setTabText(self.PredictionSubTabWidget.indexOf(self.altura), QCoreApplication.translate("AMS_Interface", u"Altura das Camadas", None))
        self.test_label.setText(QCoreApplication.translate("AMS_Interface", u"TextLabel", None))
        self.PredictionSubTabWidget.setTabText(self.PredictionSubTabWidget.indexOf(self.redes_neurais_geometria), QCoreApplication.translate("AMS_Interface", u"Redes Neurais Geometria", None))
        self.PredictionSubTabWidget.setTabText(self.PredictionSubTabWidget.indexOf(self.balanco_fase), QCoreApplication.translate("AMS_Interface", u"Balan\u00e7o de Fase", None))
        self.PredictionSubTabWidget.setTabText(self.PredictionSubTabWidget.indexOf(self.distancia_interdendritica), QCoreApplication.translate("AMS_Interface", u"Dist\u00e2ncia Interdendr\u00edtica", None))
        self.PredictionSubTabWidget.setTabText(self.PredictionSubTabWidget.indexOf(self.tamanho_grao), QCoreApplication.translate("AMS_Interface", u"Tamanho de Gr\u00e3o", None))
        self.primaryTabWidget.setTabText(self.primaryTabWidget.indexOf(self.PredictionWidget), QCoreApplication.translate("AMS_Interface", u"Predi\u00e7\u00e3o", None))
        self.MeasureToolSubTabWidget.setTabText(self.MeasureToolSubTabWidget.indexOf(self.melting_pool), QCoreApplication.translate("AMS_Interface", u"Melting Pool", None))
        self.MeasureToolSubTabWidget.setTabText(self.MeasureToolSubTabWidget.indexOf(self.bead_geometry), QCoreApplication.translate("AMS_Interface", u"Bead Geometry", None))
        self.primaryTabWidget.setTabText(self.primaryTabWidget.indexOf(self.MeasureToolWidget), QCoreApplication.translate("AMS_Interface", u"Measuring Tool", None))
        self.primaryTabWidget.setTabText(self.primaryTabWidget.indexOf(self.tab_3), QCoreApplication.translate("AMS_Interface", u"Thermal Cycles", None))
        self.primaryTabWidget.setTabText(self.primaryTabWidget.indexOf(self.tab_4), QCoreApplication.translate("AMS_Interface", u"Point Cloud Analysis", None))
        self.primaryTabWidget.setTabText(self.primaryTabWidget.indexOf(self.tab_5), QCoreApplication.translate("AMS_Interface", u"Thermal control systems", None))
        self.primaryTabWidget.setTabText(self.primaryTabWidget.indexOf(self.tab_6), QCoreApplication.translate("AMS_Interface", u"Instability and detect monitoring", None))
    # retranslateUi


    def GeometricPredictionCallback(self, Ws, Ts, V, I, Mp, Sh, Vi, De, Ct, D):
        penetration = BeadGeometry.getPenetration(V, I, Ws, Ts, Mp, Sh)
        t_solid = BeadGeometry.getT_Sol(Sh, D, Ts, I, V, De, penetration, Mp, Ct, Ws)
        height, width = BeadGeometry.getBeadGeometry(D, Ws, Ts, I, V, t_solid, De, Sh, Vi, Ct)

        self.penetration.setText(str(round(penetration, 3)))
        self.t_solid.setText(str(round(t_solid,3)))
        print(str(height))
        #self.height.setText(str(round(height,3)))
        #self.width.setText(str(round(width,3)))


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

 