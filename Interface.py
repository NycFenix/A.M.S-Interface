from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QGridLayout, QLabel, QLineEdit,
    QMainWindow, QPushButton, QSizePolicy, QSpacerItem,
    QStatusBar, QTabWidget, QWidget)

class Ui_AMS(object):
    def setupUi(self, AMS):
        if not AMS.objectName():
            AMS.setObjectName(u"AMS")
        AMS.resize(800, 600)



        # Initializing Widgets and TabBar
        self.centralwidget = QWidget(AMS)
        self.FerramentasTab = QWidget()
        self.FerramentasSubTab = QTabWidget(self.FerramentasTab)
        self.MainTab = QTabWidget(self.centralwidget)
        self.Predicao = QWidget()
        self.PredicaoSubTab = QTabWidget
        self.Predicao1 = QWidget()
        self.Predicao2 = QWidget()
        self.Predicao3 = QWidget()
        self.gridLayoutWidget = QWidget(self.Predicao)



        self.MainTab.setGeometry(QRect(0, 0, 791, 591))
        self.gridLayoutWidget.setGeometry(QRect(120, 40, 511, 61))
        self.gridLayout = QGridLayout(self.gridLayoutWidget)
        #self.gridLayout.addWidget(self.PredicaoSubTab)


        # self.PredicaoSubTab.addTab(self.Predicao1, "Predicao 1")
        # self.PredicaoSubTab.addTab(self.Predicao2, "Predicao 2")
        # self.PredicaoSubTab.addtab
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalSpacer = QSpacerItem(1000, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)
        
        self.gridLayout.addItem(self.horizontalSpacer, 1, 1, 1, 1)

        self.lineEdit = QLineEdit(self.gridLayoutWidget)
        

        self.gridLayout.addWidget(self.lineEdit, 1, 2, 1, 1)

        self.lineEdit_3 = QLineEdit(self.gridLayoutWidget)
 

        self.gridLayout.addWidget(self.lineEdit_3, 1, 4, 1, 1)

        self.horizontalSpacer_2 = QSpacerItem(1000, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer_2, 1, 3, 1, 1)

        self.lineEdit_2 = QLineEdit(self.gridLayoutWidget)


        self.gridLayout.addWidget(self.lineEdit_2, 1, 0, 1, 1)

        self.label = QLabel(self.gridLayoutWidget)

        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)

        self.label_2 = QLabel(self.gridLayoutWidget)

        self.gridLayout.addWidget(self.label_2, 0, 2, 1, 1)

        self.label_3 = QLabel(self.gridLayoutWidget)

        self.gridLayout.addWidget(self.label_3, 0, 4, 1, 1)

        self.pushButton = QPushButton(self.Predicao)
        self.pushButton.setGeometry(QRect(320, 120, 91, 31))

        self.label_4 = QLabel(self.Predicao)
        self.label_4.setGeometry(QRect(180, 190, 371, 251))
        self.label_4.setPixmap(QPixmap("img\Diagrama-de-fases-template.png"))
        
        
        self.MainTab.addTab(self.Predicao, "")

        
        
        self.FerramentasTab.layout = QGridLayout(self.FerramentasTab)
        self.FerramentasTab.layout.addWidget(self.FerramentasSubTab)
        self.FerramentasTab.setLayout(self.FerramentasTab.layout)
        
        self.MainTab.addTab(self.FerramentasTab, "")

        self.Ferramenta1 = QWidget()
        self.Ferramenta2 = QWidget()

        self.FerramentasSubTab.addTab(self.Ferramenta1, "Ferramenta 1")
        self.FerramentasSubTab.addTab(self.Ferramenta2, "Ferramenta 2")

        # Campo Ferramenta 1
        self.Ferramenta1.layout = QGridLayout(self.FerramentasTab)
        self.Ferramenta1.setLayout(self.Ferramenta1.layout)

        # Campo Ferramenta 2
        self.Ferramenta2.layout = QGridLayout(self.FerramentasTab)
        self.Ferramenta2.setLayout(self.Ferramenta2.layout)


        self.Configuracoes = QWidget()
        self.Configuracoes.setGeometry(QRect(-1, -1, 791, 571))
        self.MainTab.addTab(self.Configuracoes, "")
        AMS.setCentralWidget(self.centralwidget)
        

        self.retranslateUi(AMS)
        self.MainTab.setCurrentIndex(1)
        QMetaObject.connectSlotsByName(AMS)
    # setupUi

    def retranslateUi(self, AMS):
        AMS.setWindowTitle(QCoreApplication.translate("AMS", u"MainWindow", None))
        self.label.setText(QCoreApplication.translate("AMS", u"Massa", None))
        self.label_2.setText(QCoreApplication.translate("AMS", u"Comprimento", None))
        self.label_3.setText(QCoreApplication.translate("AMS", u"Temperatura (Em C\u00b0)", None))
        self.pushButton.setText(QCoreApplication.translate("AMS", u"Preview", None))
        self.MainTab.setTabText(self.MainTab.indexOf(self.Predicao), QCoreApplication.translate("AMS", u"Predição", None))
        self.MainTab.setTabText(self.MainTab.indexOf(self.FerramentasTab), QCoreApplication.translate("AMS", u"FerramentasTab", None))
        self.MainTab.setTabText(self.MainTab.indexOf(self.Configuracoes), QCoreApplication.translate("AMS", u"Configurações", None))
    # retranslateUi

