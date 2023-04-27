from email.charset import QP
from  PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
import sys

from sizepolicy1 import *

class Ui_MainwindowAdapter(QMainWindow, Ui_MainWindow):
    def __init__(self,*args, **kwargs):
        super(Ui_MainwindowAdapter,self).__init__(*args, **kwargs)
        self.setupUi(self)
        # self.setFixedSize(500,200)
        # 让控件无限缩小
        # 1, setMinimumSize, 
        # 2, setPolicy = maximu
        self.setMinimumSize(1,1)
        
        # 让控件无限放大
        # 1, setMinimumSize, 
        # 2, setPolicy = minimu
        
        print("self.geometry = {}".format(self.geometry()))
        print("pushbtn geometry = {}".format(self.pushButton.geometry()))
        print("pushbtn sizehint = {}".format(self.pushButton.sizeHint()))
        
    

if __name__ == "__main__":
    app = QApplication(sys.argv)
    app.setApplicationName("test")
    window = Ui_MainwindowAdapter()
    window.show()
    sys.exit(app.exec_())