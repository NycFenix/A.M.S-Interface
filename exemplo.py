import sys
from PySide6.QtWidgets import QWidget, QVBoxLayout, QTabWidget, QApplication, QMainWindow


class MyAPP(QMainWindow):
  def __init__(self):
    super().__init__()
    
    self.setWindowTitle("PyQt5 Test")
    self.setGeometry(100, 100, 300, 300)

    self.tab_widget = MyTabWidget(self)
    self.setCentralWidget(self.tab_widget)

    self.show()

class MyTabWidget(QWidget):
  def __init__(self, parent):
    super(QWidget, self).__init__(parent)
    self.main_layout = QVBoxLayout(self)
    # Initialize tab screen
    self.tabs                = QTabWidget()
    self.connect_tab         = QWidget()
    self.non_host_tab        = QWidget()
    self.non_host_wgt        = QTabWidget()
    self.non_host_combat_tab = QWidget()
    self.non_host_other_tab  = QWidget()
    self.slider_tab          = QWidget()

    # Add tabs
    self.tabs.addTab(self.connect_tab, "Connect")
    self.tabs.addTab(self.non_host_tab, "Non-Host")
    self.tabs.addTab(self.slider_tab, "Slider")

    # Connect Tab
    self.connect_tab.layout = QVBoxLayout(self)
    # Add whatever you need in the layout here
    self.connect_tab.setLayout(self.connect_tab.layout)

    # Non-Host Widget
    self.non_host_wgt.addTab(self.non_host_combat_tab, "Combat")
    self.non_host_wgt.addTab(self.non_host_other_tab, "Other")

    # Non-Host Combat Tab
    self.non_host_combat_tab.layout = QVBoxLayout(self)
    # Add whatever you need in the layout here
    self.non_host_combat_tab.setLayout(self.non_host_combat_tab.layout)

    # Non-Host Other Tab
    self.non_host_other_tab.layout = QVBoxLayout(self)
    # Add whatever you need in the layout here
    self.non_host_other_tab.setLayout(self.non_host_other_tab.layout)

    # Non-Host Tab
    self.non_host_tab.layout = QVBoxLayout(self)
    self.non_host_tab.layout.addWidget(self.non_host_wgt)
    self.non_host_tab.setLayout(self.non_host_tab.layout)

    # Slider Tab
    self.slider_tab.layout = QVBoxLayout(self)
    # Add whatever you need in the layout here
    self.slider_tab.setLayout(self.connect_tab.layout)

    # Add Tabs to main layout
    self.main_layout.addWidget(self.tabs)
    self.setLayout(self.main_layout)

if __name__ == "__main__":
  app = QApplication(sys.argv)
  window = MyAPP()
  sys.exit(app.exec())