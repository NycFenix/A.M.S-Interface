import os
import sys
#from AMSInterface_atual import Ui_AMS_Interface
#from lib.ui import Ui_AMS_Interface
from AMSInterface import AMSInterface


from PySide6.QtWidgets import (QApplication)

from PySide6.QtGui import (QIcon)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    app.setWindowIcon(QIcon("img/icons/sold_icon.ico"))
    
    #ui = Ui_AMS_Interface()
    ui = AMSInterface()
    #ui.setupUi(QUI)
    
    sys.exit(app.exec())




