# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'AMS_uiuOVkPX.ui'
##
## Created by: Qt User Interface Compiler version 6.8.1
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
from PySide6.QtWidgets import (QApplication, QGridLayout, QLabel, QLineEdit,
    QMainWindow, QPushButton, QRadioButton, QSizePolicy,
    QSpacerItem, QTabWidget, QVBoxLayout, QWidget)
import resources_rc

class Ui_AMS_Interface(object):
    def setupUi(self, AMS_Interface):
        if not AMS_Interface.objectName():
            AMS_Interface.setObjectName(u"AMS_Interface")
        AMS_Interface.resize(931, 580)
        palette = QPalette()
        brush = QBrush(QColor(255, 85, 255, 255))
        brush.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Base, brush)
        brush1 = QBrush(QColor(255, 255, 255, 255))
        brush1.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Window, brush1)
        palette.setBrush(QPalette.Inactive, QPalette.Base, brush)
        palette.setBrush(QPalette.Inactive, QPalette.Window, brush1)
        palette.setBrush(QPalette.Disabled, QPalette.Base, brush1)
        palette.setBrush(QPalette.Disabled, QPalette.Window, brush1)
        AMS_Interface.setPalette(palette)
        AMS_Interface.setUnifiedTitleAndToolBarOnMac(False)
        self.centralwidget = QWidget(AMS_Interface)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout_10 = QGridLayout(self.centralwidget)
        self.gridLayout_10.setObjectName(u"gridLayout_10")
        self.primaryTabWidget = QTabWidget(self.centralwidget)
        self.primaryTabWidget.setObjectName(u"primaryTabWidget")
        palette1 = QPalette()
        brush2 = QBrush(QColor(255, 0, 0, 255))
        brush2.setStyle(Qt.SolidPattern)
        palette1.setBrush(QPalette.Active, QPalette.WindowText, brush2)
        palette1.setBrush(QPalette.Active, QPalette.Base, brush1)
        brush3 = QBrush(QColor(0, 0, 0, 255))
        brush3.setStyle(Qt.SolidPattern)
        palette1.setBrush(QPalette.Active, QPalette.ToolTipText, brush3)
        palette1.setBrush(QPalette.Inactive, QPalette.WindowText, brush2)
        palette1.setBrush(QPalette.Inactive, QPalette.Base, brush1)
        palette1.setBrush(QPalette.Inactive, QPalette.ToolTipText, brush3)
        palette1.setBrush(QPalette.Disabled, QPalette.ToolTipText, brush3)
        self.primaryTabWidget.setPalette(palette1)
        self.PredictionWidget = QWidget()
        self.PredictionWidget.setObjectName(u"PredictionWidget")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.PredictionWidget.sizePolicy().hasHeightForWidth())
        self.PredictionWidget.setSizePolicy(sizePolicy)
        self.PredictionWidget.setMinimumSize(QSize(0, 452))
        palette2 = QPalette()
        palette2.setBrush(QPalette.Active, QPalette.Base, brush1)
        brush4 = QBrush(QColor(214, 118, 118, 255))
        brush4.setStyle(Qt.SolidPattern)
        palette2.setBrush(QPalette.Active, QPalette.Window, brush4)
        palette2.setBrush(QPalette.Inactive, QPalette.Base, brush1)
        palette2.setBrush(QPalette.Inactive, QPalette.Window, brush4)
        palette2.setBrush(QPalette.Disabled, QPalette.Base, brush4)
        palette2.setBrush(QPalette.Disabled, QPalette.Window, brush4)
        self.PredictionWidget.setPalette(palette2)
        self.gridLayout_9 = QGridLayout(self.PredictionWidget)
        self.gridLayout_9.setObjectName(u"gridLayout_9")
        self.gridLayout_9.setContentsMargins(0, 0, 0, 0)
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
        palette4.setBrush(QPalette.Active, QPalette.WindowText, brush1)
        palette4.setBrush(QPalette.Active, QPalette.Button, brush4)
        palette4.setBrush(QPalette.Active, QPalette.Base, brush4)
        palette4.setBrush(QPalette.Active, QPalette.Window, brush4)
        palette4.setBrush(QPalette.Inactive, QPalette.WindowText, brush1)
        palette4.setBrush(QPalette.Inactive, QPalette.Button, brush4)
        palette4.setBrush(QPalette.Inactive, QPalette.Base, brush4)
        palette4.setBrush(QPalette.Inactive, QPalette.Window, brush4)
        palette4.setBrush(QPalette.Disabled, QPalette.Button, brush4)
        palette4.setBrush(QPalette.Disabled, QPalette.Base, brush4)
        palette4.setBrush(QPalette.Disabled, QPalette.Window, brush4)
        self.Geometriadocordao.setPalette(palette4)
        self.Geometriadocordao.setStyleSheet(u"\n"
"#Geometriadocordao{\n"
"	background: rgb(214, 118, 118);\n"
"}\n"
"\n"
"\n"
"/* pink title labels */\n"
"#v_label, #density_label, #melting_point_label, #viscosity_label, #specific_heat_label, #emissivity_label, #conductivity_label, #current_label, #ws_label, #ts_label, #EnthalpyFusion_label{\n"
"background-color:rgb(245, 132, 153);\n"
"color:rgb(255, 255, 255);\n"
"}\n"
"\n"
"/* dark red labels */\n"
"#electric_parameters_title, #electric_current_title, #physical_properties_title, #prediction_layers_title, #wire_characteristics_title, #geometric_prediction_title {\n"
"color:rgb(162, 23, 51);\n"
"}\n"
"\n"
"/* yellow icon labels */ \n"
"#ws_icon, #ts_icon, #v_icon, #density_icon, #emissivity_icon, #viscosity_icon, #melting_point_icon, #conductivity_icon, #specific_heat_icon, #diameter_icon, #EnthalpyFusion_icon, #DBCP_label {\n"
"color:rgb(0, 0, 0);\n"
"background-color:rgb(245, 230, 196);\n"
"font-weight: bold\n"
"}\n"
"\n"
"\n"
"/* yellow layout rectangles*/\n"
"#electric_parameters_rect, #electric_curr"
                        "ent_rect, #wire_characteristics_rect, #prediction_layers_rect, #geometric_prediction_rect, #delta_e_rect, #transfer_mode_rect {\n"
"background-color:rgb(245, 232, 220)\n"
"}\n"
"\n"
"/* the single label on transfer mode because they're special */\n"
"#transfer_mode_title {\n"
"background-color:rgb(245, 197, 159)\n"
"}\n"
"\n"
"\n"
"\n"
"")
        self.gridLayout_4 = QGridLayout(self.Geometriadocordao)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.gridLayout_4.setHorizontalSpacing(5)
        self.gridLayout_4.setVerticalSpacing(10)
        self.gridLayout_4.setContentsMargins(-1, 10, 5, 10)
        self.electric_current_rect = QWidget(self.Geometriadocordao)
        self.electric_current_rect.setObjectName(u"electric_current_rect")
        self.gridLayout = QGridLayout(self.electric_current_rect)
        self.gridLayout.setObjectName(u"gridLayout")
        self.electric_current_layout = QGridLayout()
        self.electric_current_layout.setObjectName(u"electric_current_layout")
        self.electric_current_layout.setHorizontalSpacing(10)
        self.electric_current_layout.setVerticalSpacing(5)
        self.electric_current_layout.setContentsMargins(10, -1, -1, 10)
        self.thermal_conductivity = QLineEdit(self.electric_current_rect)
        self.thermal_conductivity.setObjectName(u"thermal_conductivity")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.thermal_conductivity.sizePolicy().hasHeightForWidth())
        self.thermal_conductivity.setSizePolicy(sizePolicy1)

        self.electric_current_layout.addWidget(self.thermal_conductivity, 7, 4, 1, 2)

        self.EnthalpyFusion = QLineEdit(self.electric_current_rect)
        self.EnthalpyFusion.setObjectName(u"EnthalpyFusion")

        self.electric_current_layout.addWidget(self.EnthalpyFusion, 11, 1, 1, 1)

        self.specific_heat = QLineEdit(self.electric_current_rect)
        self.specific_heat.setObjectName(u"specific_heat")
        sizePolicy1.setHeightForWidth(self.specific_heat.sizePolicy().hasHeightForWidth())
        self.specific_heat.setSizePolicy(sizePolicy1)

        self.electric_current_layout.addWidget(self.specific_heat, 7, 1, 1, 1)

        self.conductivity_measure = QLabel(self.electric_current_rect)
        self.conductivity_measure.setObjectName(u"conductivity_measure")
        palette5 = QPalette()
        palette5.setBrush(QPalette.Active, QPalette.WindowText, brush3)
        palette5.setBrush(QPalette.Inactive, QPalette.WindowText, brush3)
        self.conductivity_measure.setPalette(palette5)
        font = QFont()
        font.setPointSize(7)
        self.conductivity_measure.setFont(font)
        self.conductivity_measure.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.electric_current_layout.addWidget(self.conductivity_measure, 7, 6, 1, 1)

        self.density_label = QLabel(self.electric_current_rect)
        self.density_label.setObjectName(u"density_label")
        palette6 = QPalette()
        palette6.setBrush(QPalette.Active, QPalette.WindowText, brush1)
        brush6 = QBrush(QColor(245, 132, 153, 255))
        brush6.setStyle(Qt.SolidPattern)
        palette6.setBrush(QPalette.Active, QPalette.Button, brush6)
        palette6.setBrush(QPalette.Active, QPalette.Text, brush1)
        palette6.setBrush(QPalette.Active, QPalette.ButtonText, brush1)
        palette6.setBrush(QPalette.Active, QPalette.Base, brush6)
        palette6.setBrush(QPalette.Active, QPalette.Window, brush6)
        brush7 = QBrush(QColor(255, 255, 255, 128))
        brush7.setStyle(Qt.SolidPattern)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette6.setBrush(QPalette.Active, QPalette.PlaceholderText, brush7)
#endif
        palette6.setBrush(QPalette.Inactive, QPalette.WindowText, brush1)
        palette6.setBrush(QPalette.Inactive, QPalette.Button, brush6)
        palette6.setBrush(QPalette.Inactive, QPalette.Text, brush1)
        palette6.setBrush(QPalette.Inactive, QPalette.ButtonText, brush1)
        palette6.setBrush(QPalette.Inactive, QPalette.Base, brush6)
        palette6.setBrush(QPalette.Inactive, QPalette.Window, brush6)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette6.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush7)
#endif
        palette6.setBrush(QPalette.Disabled, QPalette.WindowText, brush1)
        palette6.setBrush(QPalette.Disabled, QPalette.Button, brush6)
        palette6.setBrush(QPalette.Disabled, QPalette.Text, brush1)
        palette6.setBrush(QPalette.Disabled, QPalette.ButtonText, brush1)
        palette6.setBrush(QPalette.Disabled, QPalette.Base, brush6)
        palette6.setBrush(QPalette.Disabled, QPalette.Window, brush6)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette6.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush7)
#endif
        self.density_label.setPalette(palette6)
        font1 = QFont()
        font1.setPointSize(7)
        font1.setBold(True)
        font1.setKerning(False)
        self.density_label.setFont(font1)
        self.density_label.setStyleSheet(u"")
        self.density_label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.electric_current_layout.addWidget(self.density_label, 4, 4, 1, 2)

        self.emissivity_label = QLabel(self.electric_current_rect)
        self.emissivity_label.setObjectName(u"emissivity_label")
        palette7 = QPalette()
        palette7.setBrush(QPalette.Active, QPalette.WindowText, brush1)
        palette7.setBrush(QPalette.Active, QPalette.Button, brush6)
        palette7.setBrush(QPalette.Active, QPalette.Text, brush1)
        palette7.setBrush(QPalette.Active, QPalette.ButtonText, brush1)
        palette7.setBrush(QPalette.Active, QPalette.Base, brush6)
        palette7.setBrush(QPalette.Active, QPalette.Window, brush6)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette7.setBrush(QPalette.Active, QPalette.PlaceholderText, brush7)
#endif
        palette7.setBrush(QPalette.Inactive, QPalette.WindowText, brush1)
        palette7.setBrush(QPalette.Inactive, QPalette.Button, brush6)
        palette7.setBrush(QPalette.Inactive, QPalette.Text, brush1)
        palette7.setBrush(QPalette.Inactive, QPalette.ButtonText, brush1)
        palette7.setBrush(QPalette.Inactive, QPalette.Base, brush6)
        palette7.setBrush(QPalette.Inactive, QPalette.Window, brush6)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette7.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush7)
#endif
        palette7.setBrush(QPalette.Disabled, QPalette.WindowText, brush1)
        palette7.setBrush(QPalette.Disabled, QPalette.Button, brush6)
        palette7.setBrush(QPalette.Disabled, QPalette.Text, brush1)
        palette7.setBrush(QPalette.Disabled, QPalette.ButtonText, brush1)
        palette7.setBrush(QPalette.Disabled, QPalette.Base, brush6)
        palette7.setBrush(QPalette.Disabled, QPalette.Window, brush6)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette7.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush7)
#endif
        self.emissivity_label.setPalette(palette7)
        self.emissivity_label.setFont(font1)
        self.emissivity_label.setStyleSheet(u"")
        self.emissivity_label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.electric_current_layout.addWidget(self.emissivity_label, 8, 4, 1, 2)

        self.density_icon = QLabel(self.electric_current_rect)
        self.density_icon.setObjectName(u"density_icon")
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy2.setHorizontalStretch(10)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.density_icon.sizePolicy().hasHeightForWidth())
        self.density_icon.setSizePolicy(sizePolicy2)
        palette8 = QPalette()
        palette8.setBrush(QPalette.Active, QPalette.WindowText, brush3)
        brush8 = QBrush(QColor(245, 230, 196, 255))
        brush8.setStyle(Qt.SolidPattern)
        palette8.setBrush(QPalette.Active, QPalette.Button, brush8)
        palette8.setBrush(QPalette.Active, QPalette.Text, brush3)
        palette8.setBrush(QPalette.Active, QPalette.ButtonText, brush3)
        palette8.setBrush(QPalette.Active, QPalette.Base, brush8)
        palette8.setBrush(QPalette.Active, QPalette.Window, brush8)
        brush9 = QBrush(QColor(0, 0, 0, 128))
        brush9.setStyle(Qt.SolidPattern)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette8.setBrush(QPalette.Active, QPalette.PlaceholderText, brush9)
#endif
        palette8.setBrush(QPalette.Inactive, QPalette.WindowText, brush3)
        palette8.setBrush(QPalette.Inactive, QPalette.Button, brush8)
        palette8.setBrush(QPalette.Inactive, QPalette.Text, brush3)
        palette8.setBrush(QPalette.Inactive, QPalette.ButtonText, brush3)
        palette8.setBrush(QPalette.Inactive, QPalette.Base, brush8)
        palette8.setBrush(QPalette.Inactive, QPalette.Window, brush8)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette8.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush9)
#endif
        palette8.setBrush(QPalette.Disabled, QPalette.WindowText, brush3)
        palette8.setBrush(QPalette.Disabled, QPalette.Button, brush8)
        palette8.setBrush(QPalette.Disabled, QPalette.Text, brush3)
        palette8.setBrush(QPalette.Disabled, QPalette.ButtonText, brush3)
        palette8.setBrush(QPalette.Disabled, QPalette.Base, brush8)
        palette8.setBrush(QPalette.Disabled, QPalette.Window, brush8)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette8.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush9)
#endif
        self.density_icon.setPalette(palette8)
        font2 = QFont()
        font2.setBold(True)
        font2.setItalic(False)
        self.density_icon.setFont(font2)
        self.density_icon.setStyleSheet(u"background-color:rgb(245, 230, 196)")
        self.density_icon.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.electric_current_layout.addWidget(self.density_icon, 5, 3, 1, 1)

        self.viscosity_label = QLabel(self.electric_current_rect)
        self.viscosity_label.setObjectName(u"viscosity_label")
        palette9 = QPalette()
        palette9.setBrush(QPalette.Active, QPalette.WindowText, brush1)
        palette9.setBrush(QPalette.Active, QPalette.Button, brush6)
        palette9.setBrush(QPalette.Active, QPalette.Text, brush1)
        palette9.setBrush(QPalette.Active, QPalette.ButtonText, brush1)
        palette9.setBrush(QPalette.Active, QPalette.Base, brush6)
        palette9.setBrush(QPalette.Active, QPalette.Window, brush6)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette9.setBrush(QPalette.Active, QPalette.PlaceholderText, brush7)
#endif
        palette9.setBrush(QPalette.Inactive, QPalette.WindowText, brush1)
        palette9.setBrush(QPalette.Inactive, QPalette.Button, brush6)
        palette9.setBrush(QPalette.Inactive, QPalette.Text, brush1)
        palette9.setBrush(QPalette.Inactive, QPalette.ButtonText, brush1)
        palette9.setBrush(QPalette.Inactive, QPalette.Base, brush6)
        palette9.setBrush(QPalette.Inactive, QPalette.Window, brush6)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette9.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush7)
#endif
        palette9.setBrush(QPalette.Disabled, QPalette.WindowText, brush1)
        palette9.setBrush(QPalette.Disabled, QPalette.Button, brush6)
        palette9.setBrush(QPalette.Disabled, QPalette.Text, brush1)
        palette9.setBrush(QPalette.Disabled, QPalette.ButtonText, brush1)
        palette9.setBrush(QPalette.Disabled, QPalette.Base, brush6)
        palette9.setBrush(QPalette.Disabled, QPalette.Window, brush6)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette9.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush7)
#endif
        self.viscosity_label.setPalette(palette9)
        self.viscosity_label.setFont(font1)
        self.viscosity_label.setStyleSheet(u"")
        self.viscosity_label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.electric_current_layout.addWidget(self.viscosity_label, 8, 1, 1, 1)

        self.emissivity = QLineEdit(self.electric_current_rect)
        self.emissivity.setObjectName(u"emissivity")
        sizePolicy1.setHeightForWidth(self.emissivity.sizePolicy().hasHeightForWidth())
        self.emissivity.setSizePolicy(sizePolicy1)

        self.electric_current_layout.addWidget(self.emissivity, 9, 4, 1, 2)

        self.specific_heat_label = QLabel(self.electric_current_rect)
        self.specific_heat_label.setObjectName(u"specific_heat_label")
        palette10 = QPalette()
        palette10.setBrush(QPalette.Active, QPalette.WindowText, brush1)
        palette10.setBrush(QPalette.Active, QPalette.Button, brush6)
        palette10.setBrush(QPalette.Active, QPalette.Text, brush1)
        palette10.setBrush(QPalette.Active, QPalette.ButtonText, brush1)
        palette10.setBrush(QPalette.Active, QPalette.Base, brush6)
        palette10.setBrush(QPalette.Active, QPalette.Window, brush6)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette10.setBrush(QPalette.Active, QPalette.PlaceholderText, brush7)
#endif
        palette10.setBrush(QPalette.Inactive, QPalette.WindowText, brush1)
        palette10.setBrush(QPalette.Inactive, QPalette.Button, brush6)
        palette10.setBrush(QPalette.Inactive, QPalette.Text, brush1)
        palette10.setBrush(QPalette.Inactive, QPalette.ButtonText, brush1)
        palette10.setBrush(QPalette.Inactive, QPalette.Base, brush6)
        palette10.setBrush(QPalette.Inactive, QPalette.Window, brush6)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette10.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush7)
#endif
        palette10.setBrush(QPalette.Disabled, QPalette.WindowText, brush1)
        palette10.setBrush(QPalette.Disabled, QPalette.Button, brush6)
        palette10.setBrush(QPalette.Disabled, QPalette.Text, brush1)
        palette10.setBrush(QPalette.Disabled, QPalette.ButtonText, brush1)
        palette10.setBrush(QPalette.Disabled, QPalette.Base, brush6)
        palette10.setBrush(QPalette.Disabled, QPalette.Window, brush6)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette10.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush7)
#endif
        self.specific_heat_label.setPalette(palette10)
        self.specific_heat_label.setFont(font1)
        self.specific_heat_label.setStyleSheet(u"")
        self.specific_heat_label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.electric_current_layout.addWidget(self.specific_heat_label, 6, 1, 1, 1)

        self.EnthalpyFusion_label = QLabel(self.electric_current_rect)
        self.EnthalpyFusion_label.setObjectName(u"EnthalpyFusion_label")
        font3 = QFont()
        font3.setPointSize(7)
        font3.setBold(True)
        self.EnthalpyFusion_label.setFont(font3)

        self.electric_current_layout.addWidget(self.EnthalpyFusion_label, 10, 1, 1, 1)

        self.melting_point_icon = QLabel(self.electric_current_rect)
        self.melting_point_icon.setObjectName(u"melting_point_icon")
        sizePolicy2.setHeightForWidth(self.melting_point_icon.sizePolicy().hasHeightForWidth())
        self.melting_point_icon.setSizePolicy(sizePolicy2)
        palette11 = QPalette()
        palette11.setBrush(QPalette.Active, QPalette.WindowText, brush3)
        palette11.setBrush(QPalette.Active, QPalette.Button, brush8)
        palette11.setBrush(QPalette.Active, QPalette.Text, brush3)
        palette11.setBrush(QPalette.Active, QPalette.ButtonText, brush3)
        palette11.setBrush(QPalette.Active, QPalette.Base, brush8)
        palette11.setBrush(QPalette.Active, QPalette.Window, brush8)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette11.setBrush(QPalette.Active, QPalette.PlaceholderText, brush9)
#endif
        palette11.setBrush(QPalette.Inactive, QPalette.WindowText, brush3)
        palette11.setBrush(QPalette.Inactive, QPalette.Button, brush8)
        palette11.setBrush(QPalette.Inactive, QPalette.Text, brush3)
        palette11.setBrush(QPalette.Inactive, QPalette.ButtonText, brush3)
        palette11.setBrush(QPalette.Inactive, QPalette.Base, brush8)
        palette11.setBrush(QPalette.Inactive, QPalette.Window, brush8)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette11.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush9)
#endif
        palette11.setBrush(QPalette.Disabled, QPalette.WindowText, brush3)
        palette11.setBrush(QPalette.Disabled, QPalette.Button, brush8)
        palette11.setBrush(QPalette.Disabled, QPalette.Text, brush3)
        palette11.setBrush(QPalette.Disabled, QPalette.ButtonText, brush3)
        palette11.setBrush(QPalette.Disabled, QPalette.Base, brush8)
        palette11.setBrush(QPalette.Disabled, QPalette.Window, brush8)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette11.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush9)
#endif
        self.melting_point_icon.setPalette(palette11)
        self.melting_point_icon.setFont(font2)
        self.melting_point_icon.setStyleSheet(u"background-color:rgb(245, 230, 196)")
        self.melting_point_icon.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.electric_current_layout.addWidget(self.melting_point_icon, 5, 0, 1, 1)

        self.density = QLineEdit(self.electric_current_rect)
        self.density.setObjectName(u"density")
        sizePolicy1.setHeightForWidth(self.density.sizePolicy().hasHeightForWidth())
        self.density.setSizePolicy(sizePolicy1)

        self.electric_current_layout.addWidget(self.density, 5, 4, 1, 2)

        self.melting_point_label = QLabel(self.electric_current_rect)
        self.melting_point_label.setObjectName(u"melting_point_label")
        palette12 = QPalette()
        palette12.setBrush(QPalette.Active, QPalette.WindowText, brush1)
        palette12.setBrush(QPalette.Active, QPalette.Button, brush6)
        palette12.setBrush(QPalette.Active, QPalette.Text, brush1)
        palette12.setBrush(QPalette.Active, QPalette.ButtonText, brush1)
        palette12.setBrush(QPalette.Active, QPalette.Base, brush6)
        palette12.setBrush(QPalette.Active, QPalette.Window, brush6)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette12.setBrush(QPalette.Active, QPalette.PlaceholderText, brush7)
#endif
        palette12.setBrush(QPalette.Inactive, QPalette.WindowText, brush1)
        palette12.setBrush(QPalette.Inactive, QPalette.Button, brush6)
        palette12.setBrush(QPalette.Inactive, QPalette.Text, brush1)
        palette12.setBrush(QPalette.Inactive, QPalette.ButtonText, brush1)
        palette12.setBrush(QPalette.Inactive, QPalette.Base, brush6)
        palette12.setBrush(QPalette.Inactive, QPalette.Window, brush6)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette12.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush7)
#endif
        palette12.setBrush(QPalette.Disabled, QPalette.WindowText, brush1)
        palette12.setBrush(QPalette.Disabled, QPalette.Button, brush6)
        palette12.setBrush(QPalette.Disabled, QPalette.Text, brush1)
        palette12.setBrush(QPalette.Disabled, QPalette.ButtonText, brush1)
        palette12.setBrush(QPalette.Disabled, QPalette.Base, brush6)
        palette12.setBrush(QPalette.Disabled, QPalette.Window, brush6)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette12.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush7)
#endif
        self.melting_point_label.setPalette(palette12)
        self.melting_point_label.setFont(font1)
        self.melting_point_label.setStyleSheet(u"")
        self.melting_point_label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.electric_current_layout.addWidget(self.melting_point_label, 4, 1, 1, 1)

        self.conductivity_label = QLabel(self.electric_current_rect)
        self.conductivity_label.setObjectName(u"conductivity_label")
        palette13 = QPalette()
        palette13.setBrush(QPalette.Active, QPalette.WindowText, brush1)
        palette13.setBrush(QPalette.Active, QPalette.Button, brush6)
        palette13.setBrush(QPalette.Active, QPalette.Text, brush1)
        palette13.setBrush(QPalette.Active, QPalette.ButtonText, brush1)
        palette13.setBrush(QPalette.Active, QPalette.Base, brush6)
        palette13.setBrush(QPalette.Active, QPalette.Window, brush6)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette13.setBrush(QPalette.Active, QPalette.PlaceholderText, brush7)
#endif
        palette13.setBrush(QPalette.Inactive, QPalette.WindowText, brush1)
        palette13.setBrush(QPalette.Inactive, QPalette.Button, brush6)
        palette13.setBrush(QPalette.Inactive, QPalette.Text, brush1)
        palette13.setBrush(QPalette.Inactive, QPalette.ButtonText, brush1)
        palette13.setBrush(QPalette.Inactive, QPalette.Base, brush6)
        palette13.setBrush(QPalette.Inactive, QPalette.Window, brush6)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette13.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush7)
#endif
        palette13.setBrush(QPalette.Disabled, QPalette.WindowText, brush1)
        palette13.setBrush(QPalette.Disabled, QPalette.Button, brush6)
        palette13.setBrush(QPalette.Disabled, QPalette.Text, brush1)
        palette13.setBrush(QPalette.Disabled, QPalette.ButtonText, brush1)
        palette13.setBrush(QPalette.Disabled, QPalette.Base, brush6)
        palette13.setBrush(QPalette.Disabled, QPalette.Window, brush6)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette13.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush7)
#endif
        self.conductivity_label.setPalette(palette13)
        self.conductivity_label.setFont(font1)
        self.conductivity_label.setStyleSheet(u"")
        self.conductivity_label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.electric_current_layout.addWidget(self.conductivity_label, 6, 4, 1, 2)

        self.physical_properties_title = QLabel(self.electric_current_rect)
        self.physical_properties_title.setObjectName(u"physical_properties_title")
        font4 = QFont()
        font4.setPointSize(8)
        font4.setBold(True)
        self.physical_properties_title.setFont(font4)

        self.electric_current_layout.addWidget(self.physical_properties_title, 3, 0, 1, 3)

        self.viscosity_measure = QLabel(self.electric_current_rect)
        self.viscosity_measure.setObjectName(u"viscosity_measure")
        font5 = QFont()
        font5.setPointSize(8)
        self.viscosity_measure.setFont(font5)

        self.electric_current_layout.addWidget(self.viscosity_measure, 9, 2, 1, 1)

        self.viscosity_icon = QLabel(self.electric_current_rect)
        self.viscosity_icon.setObjectName(u"viscosity_icon")
        sizePolicy2.setHeightForWidth(self.viscosity_icon.sizePolicy().hasHeightForWidth())
        self.viscosity_icon.setSizePolicy(sizePolicy2)
        palette14 = QPalette()
        palette14.setBrush(QPalette.Active, QPalette.WindowText, brush3)
        palette14.setBrush(QPalette.Active, QPalette.Button, brush8)
        palette14.setBrush(QPalette.Active, QPalette.Text, brush3)
        palette14.setBrush(QPalette.Active, QPalette.ButtonText, brush3)
        palette14.setBrush(QPalette.Active, QPalette.Base, brush8)
        palette14.setBrush(QPalette.Active, QPalette.Window, brush8)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette14.setBrush(QPalette.Active, QPalette.PlaceholderText, brush9)
#endif
        palette14.setBrush(QPalette.Inactive, QPalette.WindowText, brush3)
        palette14.setBrush(QPalette.Inactive, QPalette.Button, brush8)
        palette14.setBrush(QPalette.Inactive, QPalette.Text, brush3)
        palette14.setBrush(QPalette.Inactive, QPalette.ButtonText, brush3)
        palette14.setBrush(QPalette.Inactive, QPalette.Base, brush8)
        palette14.setBrush(QPalette.Inactive, QPalette.Window, brush8)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette14.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush9)
#endif
        palette14.setBrush(QPalette.Disabled, QPalette.WindowText, brush3)
        palette14.setBrush(QPalette.Disabled, QPalette.Button, brush8)
        palette14.setBrush(QPalette.Disabled, QPalette.Text, brush3)
        palette14.setBrush(QPalette.Disabled, QPalette.ButtonText, brush3)
        palette14.setBrush(QPalette.Disabled, QPalette.Base, brush8)
        palette14.setBrush(QPalette.Disabled, QPalette.Window, brush8)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette14.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush9)
#endif
        self.viscosity_icon.setPalette(palette14)
        self.viscosity_icon.setFont(font2)
        self.viscosity_icon.setStyleSheet(u"background-color:rgb(245, 230, 196)")
        self.viscosity_icon.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.electric_current_layout.addWidget(self.viscosity_icon, 9, 0, 1, 1)

        self.emissivity_icon = QLabel(self.electric_current_rect)
        self.emissivity_icon.setObjectName(u"emissivity_icon")
        sizePolicy2.setHeightForWidth(self.emissivity_icon.sizePolicy().hasHeightForWidth())
        self.emissivity_icon.setSizePolicy(sizePolicy2)
        palette15 = QPalette()
        palette15.setBrush(QPalette.Active, QPalette.WindowText, brush3)
        palette15.setBrush(QPalette.Active, QPalette.Button, brush8)
        palette15.setBrush(QPalette.Active, QPalette.Text, brush3)
        palette15.setBrush(QPalette.Active, QPalette.ButtonText, brush3)
        palette15.setBrush(QPalette.Active, QPalette.Base, brush8)
        palette15.setBrush(QPalette.Active, QPalette.Window, brush8)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette15.setBrush(QPalette.Active, QPalette.PlaceholderText, brush9)
#endif
        palette15.setBrush(QPalette.Inactive, QPalette.WindowText, brush3)
        palette15.setBrush(QPalette.Inactive, QPalette.Button, brush8)
        palette15.setBrush(QPalette.Inactive, QPalette.Text, brush3)
        palette15.setBrush(QPalette.Inactive, QPalette.ButtonText, brush3)
        palette15.setBrush(QPalette.Inactive, QPalette.Base, brush8)
        palette15.setBrush(QPalette.Inactive, QPalette.Window, brush8)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette15.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush9)
#endif
        palette15.setBrush(QPalette.Disabled, QPalette.WindowText, brush3)
        palette15.setBrush(QPalette.Disabled, QPalette.Button, brush8)
        palette15.setBrush(QPalette.Disabled, QPalette.Text, brush3)
        palette15.setBrush(QPalette.Disabled, QPalette.ButtonText, brush3)
        palette15.setBrush(QPalette.Disabled, QPalette.Base, brush8)
        palette15.setBrush(QPalette.Disabled, QPalette.Window, brush8)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette15.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush9)
#endif
        self.emissivity_icon.setPalette(palette15)
        self.emissivity_icon.setFont(font2)
        self.emissivity_icon.setStyleSheet(u"background-color:rgb(245, 230, 196)")
        self.emissivity_icon.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.electric_current_layout.addWidget(self.emissivity_icon, 9, 3, 1, 1)

        self.melting_point = QLineEdit(self.electric_current_rect)
        self.melting_point.setObjectName(u"melting_point")
        sizePolicy1.setHeightForWidth(self.melting_point.sizePolicy().hasHeightForWidth())
        self.melting_point.setSizePolicy(sizePolicy1)

        self.electric_current_layout.addWidget(self.melting_point, 5, 1, 1, 1)

        self.viscosity = QLineEdit(self.electric_current_rect)
        self.viscosity.setObjectName(u"viscosity")
        sizePolicy1.setHeightForWidth(self.viscosity.sizePolicy().hasHeightForWidth())
        self.viscosity.setSizePolicy(sizePolicy1)

        self.electric_current_layout.addWidget(self.viscosity, 9, 1, 1, 1)

        self.specific_heat_label_2 = QLabel(self.electric_current_rect)
        self.specific_heat_label_2.setObjectName(u"specific_heat_label_2")
        palette16 = QPalette()
        palette16.setBrush(QPalette.Active, QPalette.WindowText, brush3)
        palette16.setBrush(QPalette.Inactive, QPalette.WindowText, brush3)
        self.specific_heat_label_2.setPalette(palette16)
        self.specific_heat_label_2.setFont(font)

        self.electric_current_layout.addWidget(self.specific_heat_label_2, 7, 2, 1, 1)

        self.specific_heat_icon = QLabel(self.electric_current_rect)
        self.specific_heat_icon.setObjectName(u"specific_heat_icon")
        sizePolicy2.setHeightForWidth(self.specific_heat_icon.sizePolicy().hasHeightForWidth())
        self.specific_heat_icon.setSizePolicy(sizePolicy2)
        palette17 = QPalette()
        palette17.setBrush(QPalette.Active, QPalette.WindowText, brush3)
        palette17.setBrush(QPalette.Active, QPalette.Button, brush8)
        palette17.setBrush(QPalette.Active, QPalette.Text, brush3)
        palette17.setBrush(QPalette.Active, QPalette.ButtonText, brush3)
        palette17.setBrush(QPalette.Active, QPalette.Base, brush8)
        palette17.setBrush(QPalette.Active, QPalette.Window, brush8)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette17.setBrush(QPalette.Active, QPalette.PlaceholderText, brush9)
#endif
        palette17.setBrush(QPalette.Inactive, QPalette.WindowText, brush3)
        palette17.setBrush(QPalette.Inactive, QPalette.Button, brush8)
        palette17.setBrush(QPalette.Inactive, QPalette.Text, brush3)
        palette17.setBrush(QPalette.Inactive, QPalette.ButtonText, brush3)
        palette17.setBrush(QPalette.Inactive, QPalette.Base, brush8)
        palette17.setBrush(QPalette.Inactive, QPalette.Window, brush8)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette17.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush9)
#endif
        palette17.setBrush(QPalette.Disabled, QPalette.WindowText, brush3)
        palette17.setBrush(QPalette.Disabled, QPalette.Button, brush8)
        palette17.setBrush(QPalette.Disabled, QPalette.Text, brush3)
        palette17.setBrush(QPalette.Disabled, QPalette.ButtonText, brush3)
        palette17.setBrush(QPalette.Disabled, QPalette.Base, brush8)
        palette17.setBrush(QPalette.Disabled, QPalette.Window, brush8)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette17.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush9)
#endif
        self.specific_heat_icon.setPalette(palette17)
        self.specific_heat_icon.setFont(font2)
        self.specific_heat_icon.setStyleSheet(u"background-color:rgb(245, 230, 196)")
        self.specific_heat_icon.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.electric_current_layout.addWidget(self.specific_heat_icon, 7, 0, 1, 1)

        self.EnthalpyFusion_icon = QLabel(self.electric_current_rect)
        self.EnthalpyFusion_icon.setObjectName(u"EnthalpyFusion_icon")

        self.electric_current_layout.addWidget(self.EnthalpyFusion_icon, 10, 0, 1, 1)

        self.conductivity_icon = QLabel(self.electric_current_rect)
        self.conductivity_icon.setObjectName(u"conductivity_icon")
        sizePolicy2.setHeightForWidth(self.conductivity_icon.sizePolicy().hasHeightForWidth())
        self.conductivity_icon.setSizePolicy(sizePolicy2)
        palette18 = QPalette()
        palette18.setBrush(QPalette.Active, QPalette.WindowText, brush3)
        palette18.setBrush(QPalette.Active, QPalette.Button, brush8)
        palette18.setBrush(QPalette.Active, QPalette.Text, brush3)
        palette18.setBrush(QPalette.Active, QPalette.ButtonText, brush3)
        palette18.setBrush(QPalette.Active, QPalette.Base, brush8)
        palette18.setBrush(QPalette.Active, QPalette.Window, brush8)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette18.setBrush(QPalette.Active, QPalette.PlaceholderText, brush9)
#endif
        palette18.setBrush(QPalette.Inactive, QPalette.WindowText, brush3)
        palette18.setBrush(QPalette.Inactive, QPalette.Button, brush8)
        palette18.setBrush(QPalette.Inactive, QPalette.Text, brush3)
        palette18.setBrush(QPalette.Inactive, QPalette.ButtonText, brush3)
        palette18.setBrush(QPalette.Inactive, QPalette.Base, brush8)
        palette18.setBrush(QPalette.Inactive, QPalette.Window, brush8)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette18.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush9)
#endif
        palette18.setBrush(QPalette.Disabled, QPalette.WindowText, brush3)
        palette18.setBrush(QPalette.Disabled, QPalette.Button, brush8)
        palette18.setBrush(QPalette.Disabled, QPalette.Text, brush3)
        palette18.setBrush(QPalette.Disabled, QPalette.ButtonText, brush3)
        palette18.setBrush(QPalette.Disabled, QPalette.Base, brush8)
        palette18.setBrush(QPalette.Disabled, QPalette.Window, brush8)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette18.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush9)
#endif
        self.conductivity_icon.setPalette(palette18)
        self.conductivity_icon.setFont(font2)
        self.conductivity_icon.setStyleSheet(u"background-color:rgb(245, 230, 196)")
        self.conductivity_icon.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.electric_current_layout.addWidget(self.conductivity_icon, 7, 3, 1, 1)

        self.density_measure = QLabel(self.electric_current_rect)
        self.density_measure.setObjectName(u"density_measure")
        palette19 = QPalette()
        palette19.setBrush(QPalette.Active, QPalette.WindowText, brush3)
        palette19.setBrush(QPalette.Inactive, QPalette.WindowText, brush3)
        self.density_measure.setPalette(palette19)
        self.density_measure.setFont(font)
        self.density_measure.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.electric_current_layout.addWidget(self.density_measure, 5, 6, 1, 1)

        self.melting_point_measure = QLabel(self.electric_current_rect)
        self.melting_point_measure.setObjectName(u"melting_point_measure")
        palette20 = QPalette()
        palette20.setBrush(QPalette.Active, QPalette.WindowText, brush3)
        palette20.setBrush(QPalette.Inactive, QPalette.WindowText, brush3)
        self.melting_point_measure.setPalette(palette20)
        font6 = QFont()
        font6.setPointSize(7)
        font6.setItalic(False)
        self.melting_point_measure.setFont(font6)
        self.melting_point_measure.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.electric_current_layout.addWidget(self.melting_point_measure, 5, 2, 1, 1)

        self.enthalpy_measure = QLabel(self.electric_current_rect)
        self.enthalpy_measure.setObjectName(u"enthalpy_measure")
        self.enthalpy_measure.setFont(font)
        self.enthalpy_measure.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.electric_current_layout.addWidget(self.enthalpy_measure, 10, 2, 1, 1)

        self.current_label = QLabel(self.electric_current_rect)
        self.current_label.setObjectName(u"current_label")
        palette21 = QPalette()
        palette21.setBrush(QPalette.Active, QPalette.WindowText, brush1)
        palette21.setBrush(QPalette.Active, QPalette.Button, brush6)
        palette21.setBrush(QPalette.Active, QPalette.Text, brush1)
        palette21.setBrush(QPalette.Active, QPalette.ButtonText, brush1)
        palette21.setBrush(QPalette.Active, QPalette.Base, brush6)
        palette21.setBrush(QPalette.Active, QPalette.Window, brush6)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette21.setBrush(QPalette.Active, QPalette.PlaceholderText, brush7)
#endif
        palette21.setBrush(QPalette.Inactive, QPalette.WindowText, brush1)
        palette21.setBrush(QPalette.Inactive, QPalette.Button, brush6)
        palette21.setBrush(QPalette.Inactive, QPalette.Text, brush1)
        palette21.setBrush(QPalette.Inactive, QPalette.ButtonText, brush1)
        palette21.setBrush(QPalette.Inactive, QPalette.Base, brush6)
        palette21.setBrush(QPalette.Inactive, QPalette.Window, brush6)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette21.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush7)
#endif
        palette21.setBrush(QPalette.Disabled, QPalette.WindowText, brush1)
        palette21.setBrush(QPalette.Disabled, QPalette.Button, brush6)
        palette21.setBrush(QPalette.Disabled, QPalette.Text, brush1)
        palette21.setBrush(QPalette.Disabled, QPalette.ButtonText, brush1)
        palette21.setBrush(QPalette.Disabled, QPalette.Base, brush6)
        palette21.setBrush(QPalette.Disabled, QPalette.Window, brush6)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette21.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush7)
#endif
        self.current_label.setPalette(palette21)
        font7 = QFont()
        font7.setBold(True)
        self.current_label.setFont(font7)
        self.current_label.setStyleSheet(u"")
        self.current_label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.electric_current_layout.addWidget(self.current_label, 1, 1, 1, 2)

        self.I_measure = QLabel(self.electric_current_rect)
        self.I_measure.setObjectName(u"I_measure")
        palette22 = QPalette()
        palette22.setBrush(QPalette.Active, QPalette.WindowText, brush3)
        palette22.setBrush(QPalette.Inactive, QPalette.WindowText, brush3)
        self.I_measure.setPalette(palette22)
        self.I_measure.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)

        self.electric_current_layout.addWidget(self.I_measure, 2, 3, 1, 1)

        self.I = QLineEdit(self.electric_current_rect)
        self.I.setObjectName(u"I")
        sizePolicy1.setHeightForWidth(self.I.sizePolicy().hasHeightForWidth())
        self.I.setSizePolicy(sizePolicy1)
        self.I.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.electric_current_layout.addWidget(self.I, 2, 1, 1, 2)

        self.electric_current_title = QLabel(self.electric_current_rect)
        self.electric_current_title.setObjectName(u"electric_current_title")
        self.electric_current_title.setFont(font4)

        self.electric_current_layout.addWidget(self.electric_current_title, 0, 0, 1, 4)


        self.gridLayout.addLayout(self.electric_current_layout, 0, 0, 1, 1)


        self.gridLayout_4.addWidget(self.electric_current_rect, 2, 0, 2, 4)

        self.delta_e_rect = QWidget(self.Geometriadocordao)
        self.delta_e_rect.setObjectName(u"delta_e_rect")
        self.gridLayout_6 = QGridLayout(self.delta_e_rect)
        self.gridLayout_6.setObjectName(u"gridLayout_6")
        self.delta_e_layout = QGridLayout()
        self.delta_e_layout.setObjectName(u"delta_e_layout")
        self.delta_e_label = QLabel(self.delta_e_rect)
        self.delta_e_label.setObjectName(u"delta_e_label")
        sizePolicy1.setHeightForWidth(self.delta_e_label.sizePolicy().hasHeightForWidth())
        self.delta_e_label.setSizePolicy(sizePolicy1)
        self.delta_e_label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.delta_e_layout.addWidget(self.delta_e_label, 1, 3, 1, 1)

        self.energy_button = QPushButton(self.delta_e_rect)
        self.energy_button.setObjectName(u"energy_button")
        sizePolicy.setHeightForWidth(self.energy_button.sizePolicy().hasHeightForWidth())
        self.energy_button.setSizePolicy(sizePolicy)

        self.delta_e_layout.addWidget(self.energy_button, 1, 0, 1, 1)

        self.delta_e_input = QLineEdit(self.delta_e_rect)
        self.delta_e_input.setObjectName(u"delta_e_input")
        sizePolicy3 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Maximum)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.delta_e_input.sizePolicy().hasHeightForWidth())
        self.delta_e_input.setSizePolicy(sizePolicy3)
        self.delta_e_input.setAlignment(Qt.AlignmentFlag.AlignHCenter|Qt.AlignmentFlag.AlignTop)

        self.delta_e_layout.addWidget(self.delta_e_input, 1, 2, 1, 1)


        self.gridLayout_6.addLayout(self.delta_e_layout, 0, 0, 1, 1)


        self.gridLayout_4.addWidget(self.delta_e_rect, 1, 4, 1, 1)

        self.transfer_mode_rect = QWidget(self.Geometriadocordao)
        self.transfer_mode_rect.setObjectName(u"transfer_mode_rect")
        self.verticalLayout_4 = QVBoxLayout(self.transfer_mode_rect)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.transfer_mode_title = QLabel(self.transfer_mode_rect)
        self.transfer_mode_title.setObjectName(u"transfer_mode_title")
        font8 = QFont()
        font8.setBold(True)
        font8.setItalic(True)
        self.transfer_mode_title.setFont(font8)
        self.transfer_mode_title.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_4.addWidget(self.transfer_mode_title)

        self.cmt = QRadioButton(self.transfer_mode_rect)
        self.cmt.setObjectName(u"cmt")

        self.verticalLayout_4.addWidget(self.cmt)

        self.mix = QRadioButton(self.transfer_mode_rect)
        self.mix.setObjectName(u"mix")

        self.verticalLayout_4.addWidget(self.mix)

        self.pulsado = QRadioButton(self.transfer_mode_rect)
        self.pulsado.setObjectName(u"pulsado")

        self.verticalLayout_4.addWidget(self.pulsado)


        self.gridLayout_4.addWidget(self.transfer_mode_rect, 1, 3, 1, 1)

        self.geometric_prediction_rect = QWidget(self.Geometriadocordao)
        self.geometric_prediction_rect.setObjectName(u"geometric_prediction_rect")
        self.gridLayout_7 = QGridLayout(self.geometric_prediction_rect)
        self.gridLayout_7.setObjectName(u"gridLayout_7")
        self.geometric_prediction_layout_3 = QGridLayout()
        self.geometric_prediction_layout_3.setObjectName(u"geometric_prediction_layout_3")
        self.geometric_prediction_layout_3.setHorizontalSpacing(10)
        self.geometric_prediction_layout_3.setVerticalSpacing(20)
        self.geometric_prediction_layout_3.setContentsMargins(10, -1, 10, 10)
        self.geometric_prediction_title = QLabel(self.geometric_prediction_rect)
        self.geometric_prediction_title.setObjectName(u"geometric_prediction_title")
        font9 = QFont()
        font9.setBold(True)
        font9.setKerning(True)
        self.geometric_prediction_title.setFont(font9)
        self.geometric_prediction_title.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.geometric_prediction_title.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.geometric_prediction_layout_3.addWidget(self.geometric_prediction_title, 0, 0, 1, 4)

        self.Tmax = QLineEdit(self.geometric_prediction_rect)
        self.Tmax.setObjectName(u"Tmax")
        sizePolicy4 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.Tmax.sizePolicy().hasHeightForWidth())
        self.Tmax.setSizePolicy(sizePolicy4)
        font10 = QFont()
        font10.setPointSize(10)
        self.Tmax.setFont(font10)
        self.Tmax.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.geometric_prediction_layout_3.addWidget(self.Tmax, 6, 1, 1, 2)

        self.penetration_measure = QLabel(self.geometric_prediction_rect)
        self.penetration_measure.setObjectName(u"penetration_measure")
        palette23 = QPalette()
        palette23.setBrush(QPalette.Active, QPalette.WindowText, brush3)
        palette23.setBrush(QPalette.Inactive, QPalette.WindowText, brush3)
        self.penetration_measure.setPalette(palette23)

        self.geometric_prediction_layout_3.addWidget(self.penetration_measure, 4, 3, 1, 1)

        self.height_label = QLabel(self.geometric_prediction_rect)
        self.height_label.setObjectName(u"height_label")
        palette24 = QPalette()
        palette24.setBrush(QPalette.Active, QPalette.WindowText, brush3)
        palette24.setBrush(QPalette.Inactive, QPalette.WindowText, brush3)
        self.height_label.setPalette(palette24)
        font11 = QFont()
        font11.setPointSize(11)
        self.height_label.setFont(font11)
        self.height_label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.geometric_prediction_layout_3.addWidget(self.height_label, 3, 0, 1, 1)

        self.penetration_label = QLabel(self.geometric_prediction_rect)
        self.penetration_label.setObjectName(u"penetration_label")
        palette25 = QPalette()
        palette25.setBrush(QPalette.Active, QPalette.WindowText, brush3)
        palette25.setBrush(QPalette.Inactive, QPalette.WindowText, brush3)
        self.penetration_label.setPalette(palette25)
        self.penetration_label.setFont(font10)
        self.penetration_label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.geometric_prediction_layout_3.addWidget(self.penetration_label, 4, 0, 1, 1)

        self.height_measure = QLabel(self.geometric_prediction_rect)
        self.height_measure.setObjectName(u"height_measure")
        palette26 = QPalette()
        palette26.setBrush(QPalette.Active, QPalette.WindowText, brush3)
        palette26.setBrush(QPalette.Inactive, QPalette.WindowText, brush3)
        self.height_measure.setPalette(palette26)

        self.geometric_prediction_layout_3.addWidget(self.height_measure, 3, 3, 1, 1)

        self.width_measure = QLabel(self.geometric_prediction_rect)
        self.width_measure.setObjectName(u"width_measure")
        palette27 = QPalette()
        palette27.setBrush(QPalette.Active, QPalette.WindowText, brush3)
        palette27.setBrush(QPalette.Inactive, QPalette.WindowText, brush3)
        self.width_measure.setPalette(palette27)

        self.geometric_prediction_layout_3.addWidget(self.width_measure, 2, 3, 1, 1)

        self.Tmax_label = QLabel(self.geometric_prediction_rect)
        self.Tmax_label.setObjectName(u"Tmax_label")
        self.Tmax_label.setFont(font10)
        self.Tmax_label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.geometric_prediction_layout_3.addWidget(self.Tmax_label, 6, 0, 1, 1)

        self.t_solid_label = QLabel(self.geometric_prediction_rect)
        self.t_solid_label.setObjectName(u"t_solid_label")
        palette28 = QPalette()
        palette28.setBrush(QPalette.Active, QPalette.WindowText, brush3)
        palette28.setBrush(QPalette.Inactive, QPalette.WindowText, brush3)
        self.t_solid_label.setPalette(palette28)
        self.t_solid_label.setFont(font10)
        self.t_solid_label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.geometric_prediction_layout_3.addWidget(self.t_solid_label, 5, 0, 1, 1)

        self.t_solid_measure = QLabel(self.geometric_prediction_rect)
        self.t_solid_measure.setObjectName(u"t_solid_measure")
        palette29 = QPalette()
        palette29.setBrush(QPalette.Active, QPalette.WindowText, brush3)
        palette29.setBrush(QPalette.Inactive, QPalette.WindowText, brush3)
        self.t_solid_measure.setPalette(palette29)

        self.geometric_prediction_layout_3.addWidget(self.t_solid_measure, 5, 3, 1, 1)

        self.width_label = QLabel(self.geometric_prediction_rect)
        self.width_label.setObjectName(u"width_label")
        palette30 = QPalette()
        palette30.setBrush(QPalette.Active, QPalette.WindowText, brush3)
        palette30.setBrush(QPalette.Inactive, QPalette.WindowText, brush3)
        self.width_label.setPalette(palette30)
        self.width_label.setFont(font11)
        self.width_label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.geometric_prediction_layout_3.addWidget(self.width_label, 2, 0, 1, 1)

        self.width = QLineEdit(self.geometric_prediction_rect)
        self.width.setObjectName(u"width")
        sizePolicy4.setHeightForWidth(self.width.sizePolicy().hasHeightForWidth())
        self.width.setSizePolicy(sizePolicy4)
        self.width.setMinimumSize(QSize(0, 0))
        self.width.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.width.setReadOnly(True)

        self.geometric_prediction_layout_3.addWidget(self.width, 2, 1, 1, 2)

        self.Tmax_measure = QLabel(self.geometric_prediction_rect)
        self.Tmax_measure.setObjectName(u"Tmax_measure")

        self.geometric_prediction_layout_3.addWidget(self.Tmax_measure, 6, 3, 1, 1)

        self.height = QLineEdit(self.geometric_prediction_rect)
        self.height.setObjectName(u"height")
        sizePolicy4.setHeightForWidth(self.height.sizePolicy().hasHeightForWidth())
        self.height.setSizePolicy(sizePolicy4)
        self.height.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.height.setReadOnly(True)

        self.geometric_prediction_layout_3.addWidget(self.height, 3, 1, 1, 2)

        self.t_solid = QLineEdit(self.geometric_prediction_rect)
        self.t_solid.setObjectName(u"t_solid")
        sizePolicy4.setHeightForWidth(self.t_solid.sizePolicy().hasHeightForWidth())
        self.t_solid.setSizePolicy(sizePolicy4)
        self.t_solid.setFont(font10)
        self.t_solid.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.t_solid.setReadOnly(True)

        self.geometric_prediction_layout_3.addWidget(self.t_solid, 5, 1, 1, 2)

        self.penetration = QLineEdit(self.geometric_prediction_rect)
        self.penetration.setObjectName(u"penetration")
        sizePolicy4.setHeightForWidth(self.penetration.sizePolicy().hasHeightForWidth())
        self.penetration.setSizePolicy(sizePolicy4)
        self.penetration.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.penetration.setReadOnly(True)

        self.geometric_prediction_layout_3.addWidget(self.penetration, 4, 1, 1, 2)

        self.calculate_button = QPushButton(self.geometric_prediction_rect)
        self.calculate_button.setObjectName(u"calculate_button")
        sizePolicy4.setHeightForWidth(self.calculate_button.sizePolicy().hasHeightForWidth())
        self.calculate_button.setSizePolicy(sizePolicy4)
        self.calculate_button.setMinimumSize(QSize(0, 20))
        palette31 = QPalette()
        brush10 = QBrush(QColor(158, 31, 34, 255))
        brush10.setStyle(Qt.SolidPattern)
        palette31.setBrush(QPalette.Active, QPalette.WindowText, brush10)
        palette31.setBrush(QPalette.Active, QPalette.ButtonText, brush10)
        palette31.setBrush(QPalette.Inactive, QPalette.WindowText, brush10)
        palette31.setBrush(QPalette.Inactive, QPalette.ButtonText, brush10)
        self.calculate_button.setPalette(palette31)

        self.geometric_prediction_layout_3.addWidget(self.calculate_button, 1, 0, 1, 4)


        self.gridLayout_7.addLayout(self.geometric_prediction_layout_3, 0, 0, 1, 1)


        self.gridLayout_4.addWidget(self.geometric_prediction_rect, 1, 5, 3, 1)

        self.electric_parameters_rect = QWidget(self.Geometriadocordao)
        self.electric_parameters_rect.setObjectName(u"electric_parameters_rect")
        self.gridLayout_2 = QGridLayout(self.electric_parameters_rect)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.electric_parameters_layout = QGridLayout()
        self.electric_parameters_layout.setObjectName(u"electric_parameters_layout")
        self.electric_parameters_layout.setHorizontalSpacing(20)
        self.electric_parameters_layout.setVerticalSpacing(5)
        self.electric_parameters_layout.setContentsMargins(-1, -1, -1, 0)
        self.v_measure = QLabel(self.electric_parameters_rect)
        self.v_measure.setObjectName(u"v_measure")
        palette32 = QPalette()
        palette32.setBrush(QPalette.Active, QPalette.WindowText, brush3)
        palette32.setBrush(QPalette.Inactive, QPalette.WindowText, brush3)
        self.v_measure.setPalette(palette32)
        self.v_measure.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.electric_parameters_layout.addWidget(self.v_measure, 8, 2, 1, 1)

        self.ws_measure1 = QLabel(self.electric_parameters_rect)
        self.ws_measure1.setObjectName(u"ws_measure1")
        sizePolicy4.setHeightForWidth(self.ws_measure1.sizePolicy().hasHeightForWidth())
        self.ws_measure1.setSizePolicy(sizePolicy4)
        palette33 = QPalette()
        palette33.setBrush(QPalette.Active, QPalette.WindowText, brush3)
        palette33.setBrush(QPalette.Inactive, QPalette.WindowText, brush3)
        self.ws_measure1.setPalette(palette33)
        self.ws_measure1.setStyleSheet(u"")
        self.ws_measure1.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.electric_parameters_layout.addWidget(self.ws_measure1, 2, 2, 1, 1)

        self.v_label = QLabel(self.electric_parameters_rect)
        self.v_label.setObjectName(u"v_label")
        palette34 = QPalette()
        palette34.setBrush(QPalette.Active, QPalette.WindowText, brush1)
        palette34.setBrush(QPalette.Active, QPalette.Button, brush6)
        brush11 = QBrush(QColor(255, 85, 0, 255))
        brush11.setStyle(Qt.SolidPattern)
        palette34.setBrush(QPalette.Active, QPalette.Light, brush11)
        palette34.setBrush(QPalette.Active, QPalette.Text, brush1)
        palette34.setBrush(QPalette.Active, QPalette.ButtonText, brush1)
        palette34.setBrush(QPalette.Active, QPalette.Base, brush6)
        palette34.setBrush(QPalette.Active, QPalette.Window, brush6)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette34.setBrush(QPalette.Active, QPalette.PlaceholderText, brush7)
#endif
        palette34.setBrush(QPalette.Inactive, QPalette.WindowText, brush1)
        palette34.setBrush(QPalette.Inactive, QPalette.Button, brush6)
        palette34.setBrush(QPalette.Inactive, QPalette.Light, brush11)
        palette34.setBrush(QPalette.Inactive, QPalette.Text, brush1)
        palette34.setBrush(QPalette.Inactive, QPalette.ButtonText, brush1)
        palette34.setBrush(QPalette.Inactive, QPalette.Base, brush6)
        palette34.setBrush(QPalette.Inactive, QPalette.Window, brush6)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette34.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush7)
#endif
        palette34.setBrush(QPalette.Disabled, QPalette.WindowText, brush1)
        palette34.setBrush(QPalette.Disabled, QPalette.Button, brush6)
        palette34.setBrush(QPalette.Disabled, QPalette.Light, brush11)
        palette34.setBrush(QPalette.Disabled, QPalette.Text, brush1)
        palette34.setBrush(QPalette.Disabled, QPalette.ButtonText, brush1)
        palette34.setBrush(QPalette.Disabled, QPalette.Base, brush6)
        palette34.setBrush(QPalette.Disabled, QPalette.Window, brush6)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette34.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush7)
#endif
        self.v_label.setPalette(palette34)
        self.v_label.setFont(font7)
        self.v_label.setStyleSheet(u"")
        self.v_label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.electric_parameters_layout.addWidget(self.v_label, 7, 1, 1, 1)

        self.ts_measure2 = QLabel(self.electric_parameters_rect)
        self.ts_measure2.setObjectName(u"ts_measure2")
        palette35 = QPalette()
        palette35.setBrush(QPalette.Active, QPalette.WindowText, brush3)
        palette35.setBrush(QPalette.Inactive, QPalette.WindowText, brush3)
        self.ts_measure2.setPalette(palette35)
        self.ts_measure2.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.electric_parameters_layout.addWidget(self.ts_measure2, 6, 2, 1, 1)

        self.ts_label = QLabel(self.electric_parameters_rect)
        self.ts_label.setObjectName(u"ts_label")
        palette36 = QPalette()
        palette36.setBrush(QPalette.Active, QPalette.WindowText, brush1)
        palette36.setBrush(QPalette.Active, QPalette.Button, brush6)
        palette36.setBrush(QPalette.Active, QPalette.Light, brush11)
        palette36.setBrush(QPalette.Active, QPalette.Text, brush1)
        palette36.setBrush(QPalette.Active, QPalette.ButtonText, brush1)
        palette36.setBrush(QPalette.Active, QPalette.Base, brush6)
        palette36.setBrush(QPalette.Active, QPalette.Window, brush6)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette36.setBrush(QPalette.Active, QPalette.PlaceholderText, brush7)
#endif
        palette36.setBrush(QPalette.Inactive, QPalette.WindowText, brush1)
        palette36.setBrush(QPalette.Inactive, QPalette.Button, brush6)
        palette36.setBrush(QPalette.Inactive, QPalette.Light, brush11)
        palette36.setBrush(QPalette.Inactive, QPalette.Text, brush1)
        palette36.setBrush(QPalette.Inactive, QPalette.ButtonText, brush1)
        palette36.setBrush(QPalette.Inactive, QPalette.Base, brush6)
        palette36.setBrush(QPalette.Inactive, QPalette.Window, brush6)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette36.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush7)
#endif
        palette36.setBrush(QPalette.Disabled, QPalette.WindowText, brush1)
        palette36.setBrush(QPalette.Disabled, QPalette.Button, brush6)
        palette36.setBrush(QPalette.Disabled, QPalette.Light, brush11)
        palette36.setBrush(QPalette.Disabled, QPalette.Text, brush1)
        palette36.setBrush(QPalette.Disabled, QPalette.ButtonText, brush1)
        palette36.setBrush(QPalette.Disabled, QPalette.Base, brush6)
        palette36.setBrush(QPalette.Disabled, QPalette.Window, brush6)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette36.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush7)
#endif
        self.ts_label.setPalette(palette36)
        self.ts_label.setFont(font7)
        self.ts_label.setStyleSheet(u"")
        self.ts_label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.electric_parameters_layout.addWidget(self.ts_label, 4, 1, 1, 1)

        self.v_icon = QLabel(self.electric_parameters_rect)
        self.v_icon.setObjectName(u"v_icon")
        sizePolicy2.setHeightForWidth(self.v_icon.sizePolicy().hasHeightForWidth())
        self.v_icon.setSizePolicy(sizePolicy2)
        palette37 = QPalette()
        palette37.setBrush(QPalette.Active, QPalette.WindowText, brush3)
        palette37.setBrush(QPalette.Active, QPalette.Button, brush8)
        palette37.setBrush(QPalette.Active, QPalette.Text, brush3)
        palette37.setBrush(QPalette.Active, QPalette.ButtonText, brush3)
        palette37.setBrush(QPalette.Active, QPalette.Base, brush8)
        palette37.setBrush(QPalette.Active, QPalette.Window, brush8)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette37.setBrush(QPalette.Active, QPalette.PlaceholderText, brush9)
#endif
        palette37.setBrush(QPalette.Inactive, QPalette.WindowText, brush3)
        palette37.setBrush(QPalette.Inactive, QPalette.Button, brush8)
        palette37.setBrush(QPalette.Inactive, QPalette.Text, brush3)
        palette37.setBrush(QPalette.Inactive, QPalette.ButtonText, brush3)
        palette37.setBrush(QPalette.Inactive, QPalette.Base, brush8)
        palette37.setBrush(QPalette.Inactive, QPalette.Window, brush8)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette37.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush9)
#endif
        palette37.setBrush(QPalette.Disabled, QPalette.WindowText, brush3)
        palette37.setBrush(QPalette.Disabled, QPalette.Button, brush8)
        palette37.setBrush(QPalette.Disabled, QPalette.Text, brush3)
        palette37.setBrush(QPalette.Disabled, QPalette.ButtonText, brush3)
        palette37.setBrush(QPalette.Disabled, QPalette.Base, brush8)
        palette37.setBrush(QPalette.Disabled, QPalette.Window, brush8)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette37.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush9)
#endif
        self.v_icon.setPalette(palette37)
        self.v_icon.setFont(font2)
        self.v_icon.setStyleSheet(u"background-color:rgb(245, 230, 196)")
        self.v_icon.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.electric_parameters_layout.addWidget(self.v_icon, 7, 0, 1, 1)

        self.ws_measure2 = QLabel(self.electric_parameters_rect)
        self.ws_measure2.setObjectName(u"ws_measure2")
        palette38 = QPalette()
        palette38.setBrush(QPalette.Active, QPalette.WindowText, brush3)
        palette38.setBrush(QPalette.Inactive, QPalette.WindowText, brush3)
        self.ws_measure2.setPalette(palette38)
        self.ws_measure2.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.electric_parameters_layout.addWidget(self.ws_measure2, 3, 2, 1, 1)

        self.ts_measure1 = QLabel(self.electric_parameters_rect)
        self.ts_measure1.setObjectName(u"ts_measure1")
        palette39 = QPalette()
        palette39.setBrush(QPalette.Active, QPalette.WindowText, brush3)
        palette39.setBrush(QPalette.Inactive, QPalette.WindowText, brush3)
        self.ts_measure1.setPalette(palette39)
        self.ts_measure1.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.electric_parameters_layout.addWidget(self.ts_measure1, 5, 2, 1, 1)

        self.ws_input1 = QLineEdit(self.electric_parameters_rect)
        self.ws_input1.setObjectName(u"ws_input1")
        self.ws_input1.setEnabled(True)
        sizePolicy4.setHeightForWidth(self.ws_input1.sizePolicy().hasHeightForWidth())
        self.ws_input1.setSizePolicy(sizePolicy4)

        self.electric_parameters_layout.addWidget(self.ws_input1, 2, 1, 1, 1)

        self.ws_input2 = QLineEdit(self.electric_parameters_rect)
        self.ws_input2.setObjectName(u"ws_input2")
        sizePolicy4.setHeightForWidth(self.ws_input2.sizePolicy().hasHeightForWidth())
        self.ws_input2.setSizePolicy(sizePolicy4)

        self.electric_parameters_layout.addWidget(self.ws_input2, 3, 1, 1, 1)

        self.v_input = QLineEdit(self.electric_parameters_rect)
        self.v_input.setObjectName(u"v_input")
        sizePolicy.setHeightForWidth(self.v_input.sizePolicy().hasHeightForWidth())
        self.v_input.setSizePolicy(sizePolicy)

        self.electric_parameters_layout.addWidget(self.v_input, 8, 1, 1, 1)

        self.ts_input2 = QLineEdit(self.electric_parameters_rect)
        self.ts_input2.setObjectName(u"ts_input2")
        sizePolicy.setHeightForWidth(self.ts_input2.sizePolicy().hasHeightForWidth())
        self.ts_input2.setSizePolicy(sizePolicy)

        self.electric_parameters_layout.addWidget(self.ts_input2, 6, 1, 1, 1)

        self.ws_label = QLabel(self.electric_parameters_rect)
        self.ws_label.setObjectName(u"ws_label")
        sizePolicy4.setHeightForWidth(self.ws_label.sizePolicy().hasHeightForWidth())
        self.ws_label.setSizePolicy(sizePolicy4)
        self.ws_label.setMinimumSize(QSize(87, 0))
        palette40 = QPalette()
        palette40.setBrush(QPalette.Active, QPalette.WindowText, brush1)
        palette40.setBrush(QPalette.Active, QPalette.Button, brush6)
        palette40.setBrush(QPalette.Active, QPalette.Light, brush11)
        palette40.setBrush(QPalette.Active, QPalette.Text, brush1)
        palette40.setBrush(QPalette.Active, QPalette.ButtonText, brush1)
        palette40.setBrush(QPalette.Active, QPalette.Base, brush6)
        palette40.setBrush(QPalette.Active, QPalette.Window, brush6)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette40.setBrush(QPalette.Active, QPalette.PlaceholderText, brush7)
#endif
        palette40.setBrush(QPalette.Inactive, QPalette.WindowText, brush1)
        palette40.setBrush(QPalette.Inactive, QPalette.Button, brush6)
        palette40.setBrush(QPalette.Inactive, QPalette.Light, brush11)
        palette40.setBrush(QPalette.Inactive, QPalette.Text, brush1)
        palette40.setBrush(QPalette.Inactive, QPalette.ButtonText, brush1)
        palette40.setBrush(QPalette.Inactive, QPalette.Base, brush6)
        palette40.setBrush(QPalette.Inactive, QPalette.Window, brush6)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette40.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush7)
#endif
        palette40.setBrush(QPalette.Disabled, QPalette.WindowText, brush1)
        palette40.setBrush(QPalette.Disabled, QPalette.Button, brush6)
        palette40.setBrush(QPalette.Disabled, QPalette.Light, brush11)
        palette40.setBrush(QPalette.Disabled, QPalette.Text, brush1)
        palette40.setBrush(QPalette.Disabled, QPalette.ButtonText, brush1)
        palette40.setBrush(QPalette.Disabled, QPalette.Base, brush6)
        palette40.setBrush(QPalette.Disabled, QPalette.Window, brush6)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette40.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush7)
#endif
        self.ws_label.setPalette(palette40)
        self.ws_label.setFont(font4)
        self.ws_label.setStyleSheet(u"")
        self.ws_label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.electric_parameters_layout.addWidget(self.ws_label, 1, 1, 1, 1)

        self.ws_icon = QLabel(self.electric_parameters_rect)
        self.ws_icon.setObjectName(u"ws_icon")
        sizePolicy5 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        sizePolicy5.setHorizontalStretch(10)
        sizePolicy5.setVerticalStretch(5)
        sizePolicy5.setHeightForWidth(self.ws_icon.sizePolicy().hasHeightForWidth())
        self.ws_icon.setSizePolicy(sizePolicy5)
        palette41 = QPalette()
        palette41.setBrush(QPalette.Active, QPalette.WindowText, brush3)
        palette41.setBrush(QPalette.Active, QPalette.Button, brush8)
        palette41.setBrush(QPalette.Active, QPalette.Text, brush3)
        palette41.setBrush(QPalette.Active, QPalette.ButtonText, brush3)
        palette41.setBrush(QPalette.Active, QPalette.Base, brush8)
        palette41.setBrush(QPalette.Active, QPalette.Window, brush8)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette41.setBrush(QPalette.Active, QPalette.PlaceholderText, brush9)
#endif
        palette41.setBrush(QPalette.Inactive, QPalette.WindowText, brush3)
        palette41.setBrush(QPalette.Inactive, QPalette.Button, brush8)
        palette41.setBrush(QPalette.Inactive, QPalette.Text, brush3)
        palette41.setBrush(QPalette.Inactive, QPalette.ButtonText, brush3)
        palette41.setBrush(QPalette.Inactive, QPalette.Base, brush8)
        palette41.setBrush(QPalette.Inactive, QPalette.Window, brush8)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette41.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush9)
#endif
        palette41.setBrush(QPalette.Disabled, QPalette.WindowText, brush3)
        palette41.setBrush(QPalette.Disabled, QPalette.Button, brush8)
        palette41.setBrush(QPalette.Disabled, QPalette.Text, brush3)
        palette41.setBrush(QPalette.Disabled, QPalette.ButtonText, brush3)
        palette41.setBrush(QPalette.Disabled, QPalette.Base, brush8)
        palette41.setBrush(QPalette.Disabled, QPalette.Window, brush8)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette41.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush9)
#endif
        self.ws_icon.setPalette(palette41)
        self.ws_icon.setFont(font2)
        self.ws_icon.setStyleSheet(u"background-color:rgb(245, 230, 196)")
        self.ws_icon.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.electric_parameters_layout.addWidget(self.ws_icon, 2, 0, 1, 1)

        self.ts_input1 = QLineEdit(self.electric_parameters_rect)
        self.ts_input1.setObjectName(u"ts_input1")
        sizePolicy.setHeightForWidth(self.ts_input1.sizePolicy().hasHeightForWidth())
        self.ts_input1.setSizePolicy(sizePolicy)

        self.electric_parameters_layout.addWidget(self.ts_input1, 5, 1, 1, 1)

        self.ts_icon = QLabel(self.electric_parameters_rect)
        self.ts_icon.setObjectName(u"ts_icon")
        sizePolicy2.setHeightForWidth(self.ts_icon.sizePolicy().hasHeightForWidth())
        self.ts_icon.setSizePolicy(sizePolicy2)
        palette42 = QPalette()
        palette42.setBrush(QPalette.Active, QPalette.WindowText, brush3)
        palette42.setBrush(QPalette.Active, QPalette.Button, brush8)
        palette42.setBrush(QPalette.Active, QPalette.Text, brush3)
        palette42.setBrush(QPalette.Active, QPalette.ButtonText, brush3)
        palette42.setBrush(QPalette.Active, QPalette.Base, brush8)
        palette42.setBrush(QPalette.Active, QPalette.Window, brush8)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette42.setBrush(QPalette.Active, QPalette.PlaceholderText, brush9)
#endif
        palette42.setBrush(QPalette.Inactive, QPalette.WindowText, brush3)
        palette42.setBrush(QPalette.Inactive, QPalette.Button, brush8)
        palette42.setBrush(QPalette.Inactive, QPalette.Text, brush3)
        palette42.setBrush(QPalette.Inactive, QPalette.ButtonText, brush3)
        palette42.setBrush(QPalette.Inactive, QPalette.Base, brush8)
        palette42.setBrush(QPalette.Inactive, QPalette.Window, brush8)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette42.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush9)
#endif
        palette42.setBrush(QPalette.Disabled, QPalette.WindowText, brush3)
        palette42.setBrush(QPalette.Disabled, QPalette.Button, brush8)
        palette42.setBrush(QPalette.Disabled, QPalette.Text, brush3)
        palette42.setBrush(QPalette.Disabled, QPalette.ButtonText, brush3)
        palette42.setBrush(QPalette.Disabled, QPalette.Base, brush8)
        palette42.setBrush(QPalette.Disabled, QPalette.Window, brush8)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette42.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush9)
#endif
        self.ts_icon.setPalette(palette42)
        self.ts_icon.setFont(font2)
        self.ts_icon.setStyleSheet(u"background-color:rgb(245, 230, 196)")
        self.ts_icon.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.electric_parameters_layout.addWidget(self.ts_icon, 4, 0, 1, 1)

        self.electric_parameters_title = QLabel(self.electric_parameters_rect)
        self.electric_parameters_title.setObjectName(u"electric_parameters_title")
        sizePolicy6 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Minimum)
        sizePolicy6.setHorizontalStretch(0)
        sizePolicy6.setVerticalStretch(0)
        sizePolicy6.setHeightForWidth(self.electric_parameters_title.sizePolicy().hasHeightForWidth())
        self.electric_parameters_title.setSizePolicy(sizePolicy6)
        self.electric_parameters_title.setFont(font7)

        self.electric_parameters_layout.addWidget(self.electric_parameters_title, 0, 0, 1, 3)


        self.gridLayout_2.addLayout(self.electric_parameters_layout, 0, 0, 1, 1)


        self.gridLayout_4.addWidget(self.electric_parameters_rect, 1, 0, 1, 3)

        self.wire_characteristics_rect = QWidget(self.Geometriadocordao)
        self.wire_characteristics_rect.setObjectName(u"wire_characteristics_rect")
        self.gridLayout_3 = QGridLayout(self.wire_characteristics_rect)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.wire_characteristics_layout = QGridLayout()
        self.wire_characteristics_layout.setSpacing(20)
        self.wire_characteristics_layout.setObjectName(u"wire_characteristics_layout")
        self.wire_characteristics_layout.setContentsMargins(10, -1, 20, 10)
        self.wire_characteristics_title = QLabel(self.wire_characteristics_rect)
        self.wire_characteristics_title.setObjectName(u"wire_characteristics_title")
        self.wire_characteristics_title.setFont(font7)
        self.wire_characteristics_title.setStyleSheet(u"")
        self.wire_characteristics_title.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.wire_characteristics_layout.addWidget(self.wire_characteristics_title, 0, 0, 1, 3)

        self.diameter_icon = QLabel(self.wire_characteristics_rect)
        self.diameter_icon.setObjectName(u"diameter_icon")
        self.diameter_icon.setEnabled(True)
        sizePolicy4.setHeightForWidth(self.diameter_icon.sizePolicy().hasHeightForWidth())
        self.diameter_icon.setSizePolicy(sizePolicy4)
        self.diameter_icon.setMinimumSize(QSize(50, 0))
        palette43 = QPalette()
        palette43.setBrush(QPalette.Active, QPalette.WindowText, brush3)
        palette43.setBrush(QPalette.Active, QPalette.Button, brush8)
        palette43.setBrush(QPalette.Active, QPalette.Text, brush3)
        palette43.setBrush(QPalette.Active, QPalette.ButtonText, brush3)
        palette43.setBrush(QPalette.Active, QPalette.Base, brush8)
        palette43.setBrush(QPalette.Active, QPalette.Window, brush8)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette43.setBrush(QPalette.Active, QPalette.PlaceholderText, brush9)
#endif
        palette43.setBrush(QPalette.Inactive, QPalette.WindowText, brush3)
        palette43.setBrush(QPalette.Inactive, QPalette.Button, brush8)
        palette43.setBrush(QPalette.Inactive, QPalette.Text, brush3)
        palette43.setBrush(QPalette.Inactive, QPalette.ButtonText, brush3)
        palette43.setBrush(QPalette.Inactive, QPalette.Base, brush8)
        palette43.setBrush(QPalette.Inactive, QPalette.Window, brush8)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette43.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush9)
#endif
        palette43.setBrush(QPalette.Disabled, QPalette.WindowText, brush3)
        palette43.setBrush(QPalette.Disabled, QPalette.Button, brush8)
        palette43.setBrush(QPalette.Disabled, QPalette.Text, brush3)
        palette43.setBrush(QPalette.Disabled, QPalette.ButtonText, brush3)
        palette43.setBrush(QPalette.Disabled, QPalette.Base, brush8)
        palette43.setBrush(QPalette.Disabled, QPalette.Window, brush8)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette43.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush9)
#endif
        self.diameter_icon.setPalette(palette43)
        self.diameter_icon.setFont(font4)
        self.diameter_icon.setStyleSheet(u"background-color:rgb(245, 230, 196)")
        self.diameter_icon.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.wire_characteristics_layout.addWidget(self.diameter_icon, 1, 0, 1, 1)

        self.diameter_measure = QLabel(self.wire_characteristics_rect)
        self.diameter_measure.setObjectName(u"diameter_measure")
        palette44 = QPalette()
        palette44.setBrush(QPalette.Active, QPalette.WindowText, brush3)
        palette44.setBrush(QPalette.Inactive, QPalette.WindowText, brush3)
        self.diameter_measure.setPalette(palette44)

        self.wire_characteristics_layout.addWidget(self.diameter_measure, 1, 2, 1, 1)

        self.diameter = QLineEdit(self.wire_characteristics_rect)
        self.diameter.setObjectName(u"diameter")
        sizePolicy7 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Fixed)
        sizePolicy7.setHorizontalStretch(0)
        sizePolicy7.setVerticalStretch(0)
        sizePolicy7.setHeightForWidth(self.diameter.sizePolicy().hasHeightForWidth())
        self.diameter.setSizePolicy(sizePolicy7)

        self.wire_characteristics_layout.addWidget(self.diameter, 1, 1, 1, 1)

        self.DBCP_label = QLabel(self.wire_characteristics_rect)
        self.DBCP_label.setObjectName(u"DBCP_label")
        sizePolicy4.setHeightForWidth(self.DBCP_label.sizePolicy().hasHeightForWidth())
        self.DBCP_label.setSizePolicy(sizePolicy4)

        self.wire_characteristics_layout.addWidget(self.DBCP_label, 2, 0, 1, 1)

        self.DBCP = QLineEdit(self.wire_characteristics_rect)
        self.DBCP.setObjectName(u"DBCP")

        self.wire_characteristics_layout.addWidget(self.DBCP, 2, 1, 1, 1)

        self.DBCP_measure = QLabel(self.wire_characteristics_rect)
        self.DBCP_measure.setObjectName(u"DBCP_measure")

        self.wire_characteristics_layout.addWidget(self.DBCP_measure, 2, 2, 1, 1)


        self.gridLayout_3.addLayout(self.wire_characteristics_layout, 0, 0, 1, 1)


        self.gridLayout_4.addWidget(self.wire_characteristics_rect, 2, 4, 2, 1)

        self.PredictionSubTabWidget.addTab(self.Geometriadocordao, "")
        self.AlturaCamadas = QWidget()
        self.AlturaCamadas.setObjectName(u"AlturaCamadas")
        palette45 = QPalette()
        brush12 = QBrush(QColor(240, 222, 200, 255))
        brush12.setStyle(Qt.SolidPattern)
        palette45.setBrush(QPalette.Active, QPalette.Button, brush12)
        palette45.setBrush(QPalette.Active, QPalette.Base, brush12)
        palette45.setBrush(QPalette.Active, QPalette.Window, brush12)
        palette45.setBrush(QPalette.Inactive, QPalette.Button, brush12)
        palette45.setBrush(QPalette.Inactive, QPalette.Base, brush12)
        palette45.setBrush(QPalette.Inactive, QPalette.Window, brush12)
        palette45.setBrush(QPalette.Disabled, QPalette.Button, brush12)
        palette45.setBrush(QPalette.Disabled, QPalette.Base, brush12)
        palette45.setBrush(QPalette.Disabled, QPalette.Window, brush12)
        self.AlturaCamadas.setPalette(palette45)
        self.AlturaCamadas.setStyleSheet(u"#AlturaCamadas{\n"
"	background-color: rgb(240, 222, 200);\n"
"}\n"
"\n"
"/*yellow layout rectangles*/\n"
"#layer_height_prediction_rect, #layer_height_result, #layer_trajectory_rect {\n"
"background-color:rgb(242, 175, 131);\n"
"}\n"
"\n"
"/*layer trajectory labels*/\n"
"#bead_width_label, #bead_overlap_label, #bead_height_label {\n"
"color:rgb(170, 39, 53);\n"
"background-color:rgb(242, 226, 187);\n"
"font-weight:bold\n"
"}\n"
"\n"
"/*layer trajectory title*/\n"
"#layer_trajectory_title, #lh_prediction_label {\n"
"color:rgb(170, 39, 53);\n"
"font-weight:bold;\n"
"text-decoration: underline;\n"
"text-decoration-color: gray;\n"
"}")
        self.gridLayout_12 = QGridLayout(self.AlturaCamadas)
        self.gridLayout_12.setObjectName(u"gridLayout_12")
        self.gridLayout_12.setHorizontalSpacing(25)
        self.gridLayout_12.setVerticalSpacing(20)
        self.layer_height_img = QWidget(self.AlturaCamadas)
        self.layer_height_img.setObjectName(u"layer_height_img")
        self.verticalLayout_2 = QVBoxLayout(self.layer_height_img)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.ImgSelector = QPushButton(self.layer_height_img)
        self.ImgSelector.setObjectName(u"ImgSelector")
        sizePolicy7.setHeightForWidth(self.ImgSelector.sizePolicy().hasHeightForWidth())
        self.ImgSelector.setSizePolicy(sizePolicy7)
        self.ImgSelector.setFlat(False)

        self.verticalLayout_2.addWidget(self.ImgSelector)

        self.ImageName_label = QLabel(self.layer_height_img)
        self.ImageName_label.setObjectName(u"ImageName_label")
        self.ImageName_label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_2.addWidget(self.ImageName_label)

        self.LayerImg = QLabel(self.layer_height_img)
        self.LayerImg.setObjectName(u"LayerImg")
        sizePolicy.setHeightForWidth(self.LayerImg.sizePolicy().hasHeightForWidth())
        self.LayerImg.setSizePolicy(sizePolicy)
        self.LayerImg.setMinimumSize(QSize(100, 200))
        self.LayerImg.setPixmap(QPixmap(u":/pictures/img/pictures/placeholderImgEvenSmaller.png"))
        self.LayerImg.setScaledContents(True)

        self.verticalLayout_2.addWidget(self.LayerImg)


        self.gridLayout_12.addWidget(self.layer_height_img, 0, 1, 1, 1)

        self.layer_height_prediction_rect = QWidget(self.AlturaCamadas)
        self.layer_height_prediction_rect.setObjectName(u"layer_height_prediction_rect")
        self.gridLayout_17 = QGridLayout(self.layer_height_prediction_rect)
        self.gridLayout_17.setObjectName(u"gridLayout_17")
        self.lh_prediction_layout = QGridLayout()
        self.lh_prediction_layout.setObjectName(u"lh_prediction_layout")
        self.lh_prediction_label = QLabel(self.layer_height_prediction_rect)
        self.lh_prediction_label.setObjectName(u"lh_prediction_label")
        self.lh_prediction_label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.lh_prediction_layout.addWidget(self.lh_prediction_label, 0, 0, 1, 1)


        self.gridLayout_17.addLayout(self.lh_prediction_layout, 0, 1, 1, 1)


        self.gridLayout_12.addWidget(self.layer_height_prediction_rect, 1, 1, 1, 1)

        self.layer_trajectory_rect = QWidget(self.AlturaCamadas)
        self.layer_trajectory_rect.setObjectName(u"layer_trajectory_rect")
        self.gridLayout_15 = QGridLayout(self.layer_trajectory_rect)
        self.gridLayout_15.setObjectName(u"gridLayout_15")
        self.gridLayout_15.setHorizontalSpacing(20)
        self.gridLayout_15.setVerticalSpacing(60)
        self.gridLayout_15.setContentsMargins(-1, 10, 9, 10)
        self.layer_trajectory_layout = QGridLayout()
        self.layer_trajectory_layout.setObjectName(u"layer_trajectory_layout")
        self.bead_overlap = QLineEdit(self.layer_trajectory_rect)
        self.bead_overlap.setObjectName(u"bead_overlap")
        sizePolicy1.setHeightForWidth(self.bead_overlap.sizePolicy().hasHeightForWidth())
        self.bead_overlap.setSizePolicy(sizePolicy1)

        self.layer_trajectory_layout.addWidget(self.bead_overlap, 3, 1, 1, 1)

        self.bead_height = QLineEdit(self.layer_trajectory_rect)
        self.bead_height.setObjectName(u"bead_height")
        sizePolicy1.setHeightForWidth(self.bead_height.sizePolicy().hasHeightForWidth())
        self.bead_height.setSizePolicy(sizePolicy1)

        self.layer_trajectory_layout.addWidget(self.bead_height, 2, 1, 1, 1)

        self.bead_overlap_label = QLabel(self.layer_trajectory_rect)
        self.bead_overlap_label.setObjectName(u"bead_overlap_label")
        self.bead_overlap_label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.layer_trajectory_layout.addWidget(self.bead_overlap_label, 3, 0, 1, 1)

        self.bead_width = QLineEdit(self.layer_trajectory_rect)
        self.bead_width.setObjectName(u"bead_width")
        sizePolicy1.setHeightForWidth(self.bead_width.sizePolicy().hasHeightForWidth())
        self.bead_width.setSizePolicy(sizePolicy1)

        self.layer_trajectory_layout.addWidget(self.bead_width, 1, 1, 1, 1)

        self.layer_trajectory_title = QLabel(self.layer_trajectory_rect)
        self.layer_trajectory_title.setObjectName(u"layer_trajectory_title")
        self.layer_trajectory_title.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.layer_trajectory_layout.addWidget(self.layer_trajectory_title, 0, 0, 1, 2)

        self.bead_height_label = QLabel(self.layer_trajectory_rect)
        self.bead_height_label.setObjectName(u"bead_height_label")
        self.bead_height_label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.layer_trajectory_layout.addWidget(self.bead_height_label, 2, 0, 1, 1)

        self.bead_width_label = QLabel(self.layer_trajectory_rect)
        self.bead_width_label.setObjectName(u"bead_width_label")
        self.bead_width_label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.layer_trajectory_layout.addWidget(self.bead_width_label, 1, 0, 1, 1)

        self.verticalSpacer_3 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Preferred)

        self.layer_trajectory_layout.addItem(self.verticalSpacer_3, 4, 1, 1, 1)


        self.gridLayout_15.addLayout(self.layer_trajectory_layout, 0, 0, 1, 1)


        self.gridLayout_12.addWidget(self.layer_trajectory_rect, 0, 0, 2, 1)

        self.layer_height_result = QWidget(self.AlturaCamadas)
        self.layer_height_result.setObjectName(u"layer_height_result")
        self.gridLayout_19 = QGridLayout(self.layer_height_result)
        self.gridLayout_19.setObjectName(u"gridLayout_19")
        self.layer_height_calculation_layout = QGridLayout()
        self.layer_height_calculation_layout.setObjectName(u"layer_height_calculation_layout")
        self.lh_label = QLabel(self.layer_height_result)
        self.lh_label.setObjectName(u"lh_label")

        self.layer_height_calculation_layout.addWidget(self.lh_label, 0, 0, 1, 1)

        self.lh_output = QLineEdit(self.layer_height_result)
        self.lh_output.setObjectName(u"lh_output")
        sizePolicy1.setHeightForWidth(self.lh_output.sizePolicy().hasHeightForWidth())
        self.lh_output.setSizePolicy(sizePolicy1)

        self.layer_height_calculation_layout.addWidget(self.lh_output, 0, 1, 1, 1)


        self.gridLayout_19.addLayout(self.layer_height_calculation_layout, 0, 0, 1, 1)


        self.gridLayout_12.addWidget(self.layer_height_result, 1, 2, 1, 1)

        self.PredictionSubTabWidget.addTab(self.AlturaCamadas, "")
        self.RedesNeuraisGeometria = QWidget()
        self.RedesNeuraisGeometria.setObjectName(u"RedesNeuraisGeometria")
        self.gridLayout_14 = QGridLayout(self.RedesNeuraisGeometria)
        self.gridLayout_14.setObjectName(u"gridLayout_14")
        self.PredictionSubTabWidget.addTab(self.RedesNeuraisGeometria, "")
        self.balanco_fase = QWidget()
        self.balanco_fase.setObjectName(u"balanco_fase")
        self.PredictionSubTabWidget.addTab(self.balanco_fase, "")
        self.distancia_interdendritica = QWidget()
        self.distancia_interdendritica.setObjectName(u"distancia_interdendritica")
        self.PredictionSubTabWidget.addTab(self.distancia_interdendritica, "")
        self.tamanho_grao = QWidget()
        self.tamanho_grao.setObjectName(u"tamanho_grao")
        self.PredictionSubTabWidget.addTab(self.tamanho_grao, "")

        self.gridLayout_9.addWidget(self.PredictionSubTabWidget, 0, 0, 1, 1)

        self.primaryTabWidget.addTab(self.PredictionWidget, "")
        self.MeasureToolWidget = QWidget()
        self.MeasureToolWidget.setObjectName(u"MeasureToolWidget")
        self.gridLayout_8 = QGridLayout(self.MeasureToolWidget)
        self.gridLayout_8.setObjectName(u"gridLayout_8")
        self.gridLayout_8.setContentsMargins(0, 0, 0, 0)
        self.MeasureToolSubTabWidget = QTabWidget(self.MeasureToolWidget)
        self.MeasureToolSubTabWidget.setObjectName(u"MeasureToolSubTabWidget")
        palette46 = QPalette()
        brush13 = QBrush(QColor(85, 170, 0, 255))
        brush13.setStyle(Qt.SolidPattern)
        palette46.setBrush(QPalette.Active, QPalette.WindowText, brush13)
        palette46.setBrush(QPalette.Inactive, QPalette.WindowText, brush13)
        self.MeasureToolSubTabWidget.setPalette(palette46)
        self.melting_pool = QWidget()
        self.melting_pool.setObjectName(u"melting_pool")
        self.melting_pool.setFont(font5)
        self.melting_pool.setStyleSheet(u"#melting_pool{\n"
"	background-color: rgb(240, 150, 150);\n"
"\n"
"}\n"
"\n"
"/*red title labels*/\n"
"#frame_extracting_title, #analysis_title, #loader_title {\n"
"color:rgb(162, 23, 51);\n"
"font-weight:bold;\n"
"text-decoration: underline;\n"
"}\n"
"\n"
"/*grey rectangle layouts*/\n"
"#ImgLoader_rect, #ExtractingFrames_rect {\n"
"background-color:rgb(240, 240, 240);\n"
"}\n"
"\n"
"/*blue buttons*/\n"
"#load_videoBttn, #MePoLoaderbttn, #LEDLoaderbttn, #Analyzebttn {\n"
"background-color:rgb(197, 252, 252);\n"
"}")
        self.gridLayout_13 = QGridLayout(self.melting_pool)
        self.gridLayout_13.setObjectName(u"gridLayout_13")
        self.gridLayout_13.setHorizontalSpacing(20)
        self.gridLayout_13.setVerticalSpacing(30)
        self.ImgLoader_rect = QWidget(self.melting_pool)
        self.ImgLoader_rect.setObjectName(u"ImgLoader_rect")
        self.verticalLayout_5 = QVBoxLayout(self.ImgLoader_rect)
        self.verticalLayout_5.setSpacing(35)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.loader_title = QLabel(self.ImgLoader_rect)
        self.loader_title.setObjectName(u"loader_title")
        self.loader_title.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_5.addWidget(self.loader_title)

        self.LEDLoaderbttn = QPushButton(self.ImgLoader_rect)
        self.LEDLoaderbttn.setObjectName(u"LEDLoaderbttn")
        sizePolicy8 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Expanding)
        sizePolicy8.setHorizontalStretch(0)
        sizePolicy8.setVerticalStretch(0)
        sizePolicy8.setHeightForWidth(self.LEDLoaderbttn.sizePolicy().hasHeightForWidth())
        self.LEDLoaderbttn.setSizePolicy(sizePolicy8)

        self.verticalLayout_5.addWidget(self.LEDLoaderbttn)

        self.MePoLoaderbttn = QPushButton(self.ImgLoader_rect)
        self.MePoLoaderbttn.setObjectName(u"MePoLoaderbttn")
        sizePolicy8.setHeightForWidth(self.MePoLoaderbttn.sizePolicy().hasHeightForWidth())
        self.MePoLoaderbttn.setSizePolicy(sizePolicy8)

        self.verticalLayout_5.addWidget(self.MePoLoaderbttn)


        self.gridLayout_13.addWidget(self.ImgLoader_rect, 2, 0, 1, 1)

        self.ExtractingFrames_rect = QWidget(self.melting_pool)
        self.ExtractingFrames_rect.setObjectName(u"ExtractingFrames_rect")
        sizePolicy4.setHeightForWidth(self.ExtractingFrames_rect.sizePolicy().hasHeightForWidth())
        self.ExtractingFrames_rect.setSizePolicy(sizePolicy4)
        self.gridLayout_16 = QGridLayout(self.ExtractingFrames_rect)
        self.gridLayout_16.setSpacing(20)
        self.gridLayout_16.setObjectName(u"gridLayout_16")
        self.Browser_label = QLabel(self.ExtractingFrames_rect)
        self.Browser_label.setObjectName(u"Browser_label")
        self.Browser_label.setFont(font7)
        self.Browser_label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout_16.addWidget(self.Browser_label, 2, 0, 1, 1)

        self.Browser_show = QLineEdit(self.ExtractingFrames_rect)
        self.Browser_show.setObjectName(u"Browser_show")

        self.gridLayout_16.addWidget(self.Browser_show, 2, 1, 1, 1)

        self.frame_extracting_title = QLabel(self.ExtractingFrames_rect)
        self.frame_extracting_title.setObjectName(u"frame_extracting_title")
        sizePolicy4.setHeightForWidth(self.frame_extracting_title.sizePolicy().hasHeightForWidth())
        self.frame_extracting_title.setSizePolicy(sizePolicy4)
        self.frame_extracting_title.setAlignment(Qt.AlignmentFlag.AlignHCenter|Qt.AlignmentFlag.AlignTop)

        self.gridLayout_16.addWidget(self.frame_extracting_title, 0, 0, 1, 2)

        self.load_videoBttn = QPushButton(self.ExtractingFrames_rect)
        self.load_videoBttn.setObjectName(u"load_videoBttn")
        sizePolicy4.setHeightForWidth(self.load_videoBttn.sizePolicy().hasHeightForWidth())
        self.load_videoBttn.setSizePolicy(sizePolicy4)

        self.gridLayout_16.addWidget(self.load_videoBttn, 1, 0, 1, 2)


        self.gridLayout_13.addWidget(self.ExtractingFrames_rect, 1, 0, 1, 1)

        self.AnalyzedImg = QLabel(self.melting_pool)
        self.AnalyzedImg.setObjectName(u"AnalyzedImg")
        sizePolicy4.setHeightForWidth(self.AnalyzedImg.sizePolicy().hasHeightForWidth())
        self.AnalyzedImg.setSizePolicy(sizePolicy4)
        self.AnalyzedImg.setPixmap(QPixmap(u":/pictures/img/pictures/placeholderImgEvenSmaller.png"))
        self.AnalyzedImg.setScaledContents(True)

        self.gridLayout_13.addWidget(self.AnalyzedImg, 1, 1, 1, 2)

        self.MeltingPoolAnalysis_rect = QWidget(self.melting_pool)
        self.MeltingPoolAnalysis_rect.setObjectName(u"MeltingPoolAnalysis_rect")
        self.verticalLayout_6 = QVBoxLayout(self.MeltingPoolAnalysis_rect)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.analysis_title = QLabel(self.MeltingPoolAnalysis_rect)
        self.analysis_title.setObjectName(u"analysis_title")
        self.analysis_title.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_6.addWidget(self.analysis_title)

        self.pushButton = QPushButton(self.MeltingPoolAnalysis_rect)
        self.pushButton.setObjectName(u"pushButton")
        sizePolicy.setHeightForWidth(self.pushButton.sizePolicy().hasHeightForWidth())
        self.pushButton.setSizePolicy(sizePolicy)

        self.verticalLayout_6.addWidget(self.pushButton)

        self.pushButton_2 = QPushButton(self.MeltingPoolAnalysis_rect)
        self.pushButton_2.setObjectName(u"pushButton_2")
        sizePolicy.setHeightForWidth(self.pushButton_2.sizePolicy().hasHeightForWidth())
        self.pushButton_2.setSizePolicy(sizePolicy)

        self.verticalLayout_6.addWidget(self.pushButton_2)

        self.pushButton_3 = QPushButton(self.MeltingPoolAnalysis_rect)
        self.pushButton_3.setObjectName(u"pushButton_3")
        sizePolicy.setHeightForWidth(self.pushButton_3.sizePolicy().hasHeightForWidth())
        self.pushButton_3.setSizePolicy(sizePolicy)

        self.verticalLayout_6.addWidget(self.pushButton_3)

        self.label = QLabel(self.MeltingPoolAnalysis_rect)
        self.label.setObjectName(u"label")
        self.label.setPixmap(QPixmap(u"../../../../Pictures/placeholderImgEvenSmaller.png"))

        self.verticalLayout_6.addWidget(self.label)


        self.gridLayout_13.addWidget(self.MeltingPoolAnalysis_rect, 1, 3, 2, 1)

        self.Analyzebttn = QPushButton(self.melting_pool)
        self.Analyzebttn.setObjectName(u"Analyzebttn")
        sizePolicy8.setHeightForWidth(self.Analyzebttn.sizePolicy().hasHeightForWidth())
        self.Analyzebttn.setSizePolicy(sizePolicy8)
        font12 = QFont()
        font12.setPointSize(12)
        font12.setBold(True)
        self.Analyzebttn.setFont(font12)

        self.gridLayout_13.addWidget(self.Analyzebttn, 0, 1, 1, 2)

        self.LEDImg = QLabel(self.melting_pool)
        self.LEDImg.setObjectName(u"LEDImg")
        self.LEDImg.setPixmap(QPixmap(u":/pictures/img/pictures/placeholderImgEvenSmaller.png"))
        self.LEDImg.setScaledContents(True)

        self.gridLayout_13.addWidget(self.LEDImg, 2, 1, 1, 1)

        self.MePoImg = QLabel(self.melting_pool)
        self.MePoImg.setObjectName(u"MePoImg")
        self.MePoImg.setPixmap(QPixmap(u":/pictures/img/pictures/placeholderImgEvenSmaller.png"))
        self.MePoImg.setScaledContents(True)

        self.gridLayout_13.addWidget(self.MePoImg, 2, 2, 1, 1)

        self.MeasureToolSubTabWidget.addTab(self.melting_pool, "")
        self.bead_geometry = QWidget()
        self.bead_geometry.setObjectName(u"bead_geometry")
        palette47 = QPalette()
        brush14 = QBrush(QColor(232, 181, 146, 255))
        brush14.setStyle(Qt.SolidPattern)
        palette47.setBrush(QPalette.Active, QPalette.Window, brush14)
        palette47.setBrush(QPalette.Inactive, QPalette.Window, brush14)
        palette47.setBrush(QPalette.Disabled, QPalette.Base, brush14)
        palette47.setBrush(QPalette.Disabled, QPalette.Window, brush14)
        self.bead_geometry.setPalette(palette47)
        self.MeasureToolSubTabWidget.addTab(self.bead_geometry, "")

        self.gridLayout_8.addWidget(self.MeasureToolSubTabWidget, 0, 0, 1, 1)

        self.primaryTabWidget.addTab(self.MeasureToolWidget, "")
        self.ThermalCyclesWidget = QWidget()
        self.ThermalCyclesWidget.setObjectName(u"ThermalCyclesWidget")
        self.primaryTabWidget.addTab(self.ThermalCyclesWidget, "")
        self.PointAnalysisWidget = QWidget()
        self.PointAnalysisWidget.setObjectName(u"PointAnalysisWidget")
        self.primaryTabWidget.addTab(self.PointAnalysisWidget, "")
        self.ThermalControlWidget = QWidget()
        self.ThermalControlWidget.setObjectName(u"ThermalControlWidget")
        self.primaryTabWidget.addTab(self.ThermalControlWidget, "")
        self.InstabilityMonitoringWidget = QWidget()
        self.InstabilityMonitoringWidget.setObjectName(u"InstabilityMonitoringWidget")
        self.primaryTabWidget.addTab(self.InstabilityMonitoringWidget, "")

        self.gridLayout_10.addWidget(self.primaryTabWidget, 0, 0, 1, 1)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout_10.addItem(self.verticalSpacer_2, 1, 0, 1, 1)

        AMS_Interface.setCentralWidget(self.centralwidget)

        self.retranslateUi(AMS_Interface)

        self.primaryTabWidget.setCurrentIndex(0)
        self.PredictionSubTabWidget.setCurrentIndex(0)
        self.MeasureToolSubTabWidget.setCurrentIndex(1)


        QMetaObject.connectSlotsByName(AMS_Interface)
    # setupUi

    def retranslateUi(self, AMS_Interface):
        AMS_Interface.setWindowTitle(QCoreApplication.translate("AMS_Interface", u"MainWindow", None))
        self.conductivity_measure.setText(QCoreApplication.translate("AMS_Interface", u"(W/(m. \u00b0K)", None))
        self.density_label.setText(QCoreApplication.translate("AMS_Interface", u"Density", None))
        self.emissivity_label.setText(QCoreApplication.translate("AMS_Interface", u"Emissivity", None))
        self.density_icon.setText(QCoreApplication.translate("AMS_Interface", u"De", None))
        self.viscosity_label.setText(QCoreApplication.translate("AMS_Interface", u"Viscosity", None))
        self.specific_heat_label.setText(QCoreApplication.translate("AMS_Interface", u"Specific Heat", None))
        self.EnthalpyFusion_label.setText(QCoreApplication.translate("AMS_Interface", u"Enthalpy of Fusion", None))
        self.melting_point_icon.setText(QCoreApplication.translate("AMS_Interface", u"Pf", None))
        self.melting_point_label.setText(QCoreApplication.translate("AMS_Interface", u"Melting Point", None))
        self.conductivity_label.setText(QCoreApplication.translate("AMS_Interface", u"Thermal Conductivity", None))
        self.physical_properties_title.setText(QCoreApplication.translate("AMS_Interface", u"Physical properties", None))
        self.viscosity_measure.setText(QCoreApplication.translate("AMS_Interface", u"g/mm*s", None))
        self.viscosity_icon.setText(QCoreApplication.translate("AMS_Interface", u"Vi", None))
        self.emissivity_icon.setText(QCoreApplication.translate("AMS_Interface", u"Em", None))
        self.specific_heat_label_2.setText(QCoreApplication.translate("AMS_Interface", u"(cal/g. \u00b0C)", None))
        self.specific_heat_icon.setText(QCoreApplication.translate("AMS_Interface", u"Ce", None))
        self.EnthalpyFusion_icon.setText(QCoreApplication.translate("AMS_Interface", u"Ef", None))
        self.conductivity_icon.setText(QCoreApplication.translate("AMS_Interface", u"Ct", None))
        self.density_measure.setText(QCoreApplication.translate("AMS_Interface", u"(g/cm^3)", None))
        self.melting_point_measure.setText(QCoreApplication.translate("AMS_Interface", u"(\u00b0C)", None))
        self.enthalpy_measure.setText(QCoreApplication.translate("AMS_Interface", u"J/g", None))
        self.current_label.setText(QCoreApplication.translate("AMS_Interface", u"Current", None))
        self.I_measure.setText(QCoreApplication.translate("AMS_Interface", u"(A)", None))
        self.electric_current_title.setText(QCoreApplication.translate("AMS_Interface", u"Electric Current", None))
        self.delta_e_label.setText(QCoreApplication.translate("AMS_Interface", u"\u0394E", None))
        self.energy_button.setText(QCoreApplication.translate("AMS_Interface", u"Delta Energy", None))
        self.transfer_mode_title.setText(QCoreApplication.translate("AMS_Interface", u"Modo de Soldagem", None))
        self.cmt.setText(QCoreApplication.translate("AMS_Interface", u"CMT", None))
        self.mix.setText(QCoreApplication.translate("AMS_Interface", u"Mix", None))
        self.pulsado.setText(QCoreApplication.translate("AMS_Interface", u"Pulsado", None))
        self.geometric_prediction_title.setText(QCoreApplication.translate("AMS_Interface", u"Geometric Prediction", None))
        self.penetration_measure.setText(QCoreApplication.translate("AMS_Interface", u"(mm)", None))
        self.height_label.setText(QCoreApplication.translate("AMS_Interface", u"Height", None))
        self.penetration_label.setText(QCoreApplication.translate("AMS_Interface", u"Penetration", None))
        self.height_measure.setText(QCoreApplication.translate("AMS_Interface", u"(mm)", None))
        self.width_measure.setText(QCoreApplication.translate("AMS_Interface", u"(mm)", None))
        self.Tmax_label.setText(QCoreApplication.translate("AMS_Interface", u"T_MAX", None))
        self.t_solid_label.setText(QCoreApplication.translate("AMS_Interface", u"t_solid", None))
        self.t_solid_measure.setText(QCoreApplication.translate("AMS_Interface", u"(s)", None))
        self.width_label.setText(QCoreApplication.translate("AMS_Interface", u"Width", None))
        self.Tmax_measure.setText(QCoreApplication.translate("AMS_Interface", u"(\u00b0C)", None))
        self.calculate_button.setText(QCoreApplication.translate("AMS_Interface", u"Calculate", None))
        self.v_measure.setText(QCoreApplication.translate("AMS_Interface", u"(V)", None))
        self.ws_measure1.setText(QCoreApplication.translate("AMS_Interface", u"(mm/s)", None))
        self.v_label.setText(QCoreApplication.translate("AMS_Interface", u"Voltage", None))
        self.ts_measure2.setText(QCoreApplication.translate("AMS_Interface", u"(m/min)", None))
        self.ts_label.setText(QCoreApplication.translate("AMS_Interface", u"Travel Speed", None))
        self.v_icon.setText(QCoreApplication.translate("AMS_Interface", u"V", None))
        self.ws_measure2.setText(QCoreApplication.translate("AMS_Interface", u"(m/min)", None))
        self.ts_measure1.setText(QCoreApplication.translate("AMS_Interface", u"(mm/s)", None))
        self.ws_label.setText(QCoreApplication.translate("AMS_Interface", u"Wire Feed Speed", None))
        self.ws_icon.setText(QCoreApplication.translate("AMS_Interface", u"Ws", None))
        self.ts_icon.setText(QCoreApplication.translate("AMS_Interface", u"Ts", None))
        self.electric_parameters_title.setText(QCoreApplication.translate("AMS_Interface", u"Electric Parameters", None))
        self.wire_characteristics_title.setText(QCoreApplication.translate("AMS_Interface", u"Wire Characteristics", None))
        self.diameter_icon.setText(QCoreApplication.translate("AMS_Interface", u"Diameter", None))
        self.diameter_measure.setText(QCoreApplication.translate("AMS_Interface", u"(mm)", None))
        self.DBCP_label.setText(QCoreApplication.translate("AMS_Interface", u"Torch-Piece Distance", None))
        self.DBCP_measure.setText(QCoreApplication.translate("AMS_Interface", u"(mm)", None))
        self.PredictionSubTabWidget.setTabText(self.PredictionSubTabWidget.indexOf(self.Geometriadocordao), QCoreApplication.translate("AMS_Interface", u"Geometria do cord\u00e3o", None))
        self.ImgSelector.setText(QCoreApplication.translate("AMS_Interface", u"Select Image:", None))
        self.ImageName_label.setText(QCoreApplication.translate("AMS_Interface", u"Image: ", None))
        self.LayerImg.setText("")
        self.lh_prediction_label.setText(QCoreApplication.translate("AMS_Interface", u"Layer height prediction, illustration images", None))
        self.bead_overlap_label.setText(QCoreApplication.translate("AMS_Interface", u"Bead Overlap", None))
        self.layer_trajectory_title.setText(QCoreApplication.translate("AMS_Interface", u"Layer trajectory characteristics", None))
        self.bead_height_label.setText(QCoreApplication.translate("AMS_Interface", u"Bead Height", None))
        self.bead_width_label.setText(QCoreApplication.translate("AMS_Interface", u"Bead Width", None))
        self.lh_label.setText(QCoreApplication.translate("AMS_Interface", u"Layer Height", None))
        self.PredictionSubTabWidget.setTabText(self.PredictionSubTabWidget.indexOf(self.AlturaCamadas), QCoreApplication.translate("AMS_Interface", u"Altura das Camadas", None))
        self.PredictionSubTabWidget.setTabText(self.PredictionSubTabWidget.indexOf(self.RedesNeuraisGeometria), QCoreApplication.translate("AMS_Interface", u"Redes Neurais Geometria", None))
        self.PredictionSubTabWidget.setTabText(self.PredictionSubTabWidget.indexOf(self.balanco_fase), QCoreApplication.translate("AMS_Interface", u"Balan\u00e7o de Fase", None))
        self.PredictionSubTabWidget.setTabText(self.PredictionSubTabWidget.indexOf(self.distancia_interdendritica), QCoreApplication.translate("AMS_Interface", u"Dist\u00e2ncia Interdendr\u00edtica", None))
        self.PredictionSubTabWidget.setTabText(self.PredictionSubTabWidget.indexOf(self.tamanho_grao), QCoreApplication.translate("AMS_Interface", u"Tamanho de Gr\u00e3o", None))
        self.primaryTabWidget.setTabText(self.primaryTabWidget.indexOf(self.PredictionWidget), QCoreApplication.translate("AMS_Interface", u"Predi\u00e7\u00e3o", None))
        self.loader_title.setText(QCoreApplication.translate("AMS_Interface", u"LOAD", None))
        self.LEDLoaderbttn.setText(QCoreApplication.translate("AMS_Interface", u"Load Image LED", None))
        self.MePoLoaderbttn.setText(QCoreApplication.translate("AMS_Interface", u"Load Image Melting Pool", None))
        self.Browser_label.setText(QCoreApplication.translate("AMS_Interface", u"Browser", None))
        self.frame_extracting_title.setText(QCoreApplication.translate("AMS_Interface", u"Extracting Frames from the video", None))
        self.load_videoBttn.setText(QCoreApplication.translate("AMS_Interface", u"Load Video", None))
        self.AnalyzedImg.setText("")
        self.analysis_title.setText(QCoreApplication.translate("AMS_Interface", u"Analysis in the melting pool", None))
        self.pushButton.setText(QCoreApplication.translate("AMS_Interface", u"Lenght and width of the weld pool", None))
        self.pushButton_2.setText(QCoreApplication.translate("AMS_Interface", u"Thermal profile in the weld pool", None))
        self.pushButton_3.setText(QCoreApplication.translate("AMS_Interface", u"Percentage of oxides in the pool", None))
        self.label.setText("")
        self.Analyzebttn.setText(QCoreApplication.translate("AMS_Interface", u"Analyze Image", None))
        self.LEDImg.setText("")
        self.MePoImg.setText("")
        self.MeasureToolSubTabWidget.setTabText(self.MeasureToolSubTabWidget.indexOf(self.melting_pool), QCoreApplication.translate("AMS_Interface", u"Melting Pool", None))
        self.MeasureToolSubTabWidget.setTabText(self.MeasureToolSubTabWidget.indexOf(self.bead_geometry), QCoreApplication.translate("AMS_Interface", u"Bead Geometry", None))
        self.primaryTabWidget.setTabText(self.primaryTabWidget.indexOf(self.MeasureToolWidget), QCoreApplication.translate("AMS_Interface", u"Measuring Tool", None))
        self.primaryTabWidget.setTabText(self.primaryTabWidget.indexOf(self.ThermalCyclesWidget), QCoreApplication.translate("AMS_Interface", u"Thermal Cycles", None))
        self.primaryTabWidget.setTabText(self.primaryTabWidget.indexOf(self.PointAnalysisWidget), QCoreApplication.translate("AMS_Interface", u"Point Cloud Analysis", None))
        self.primaryTabWidget.setTabText(self.primaryTabWidget.indexOf(self.ThermalControlWidget), QCoreApplication.translate("AMS_Interface", u"Thermal control systems", None))
        self.primaryTabWidget.setTabText(self.primaryTabWidget.indexOf(self.InstabilityMonitoringWidget), QCoreApplication.translate("AMS_Interface", u"Instability and detect monitoring", None))
    # retranslateUi

