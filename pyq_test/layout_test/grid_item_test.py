from email.charset import QP
from  PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
import sys

from ui_grid_item_test import *
    

class Ui_MainwindowAdapter(QMainWindow, Ui_MainWindow):
    def __init__(self,*args, **kwargs):
        super(Ui_MainwindowAdapter,self).__init__(*args, **kwargs)
        self.setupUi(self)
        print(self.gridLayout.indexOf(self.pushButton))
        print(self.gridLayout.indexOf(self.pushButton_2))
        print(self.gridLayout.indexOf(self.pushButton_3))
        print(self.gridLayout.indexOf(self.pushButton_4))
        print(self.gridLayout.getItemPosition(self.gridLayout.indexOf(self.pushButton)))
        print(self.gridLayout.getItemPosition(self.gridLayout.indexOf(self.pushButton_2)))
        print(self.gridLayout.getItemPosition(self.gridLayout.indexOf(self.pushButton_3)))
        print(self.gridLayout.getItemPosition(self.gridLayout.indexOf(self.pushButton_4)))
        
        
 

if __name__ == "__main__":
    app = QApplication(sys.argv)
    app.setApplicationName("test")
    window = Ui_MainwindowAdapter()
    window.show()
    sys.exit(app.exec_())
    