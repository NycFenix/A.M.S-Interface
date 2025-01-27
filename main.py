import os
import sys

from include import AMS_ui
from AMSInterface import AMSInterface

from PySide6.QtWidgets import (QApplication)
from PySide6.QtGui import (QIcon)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    #app.setWindowIcon(QIcon("img/icons/sold_icon.ico"))

    #app.setQuitOnLastWindowClosed(False)
    AMSWindow = AMSInterface()
    AMSWindow.ui.show()
    
   #ui.setupUi(QUI)
    sys.exit(app.exec())
    
