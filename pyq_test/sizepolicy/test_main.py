from email.charset import QP
from  PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
import sys

from pyq_test.sizepolicy.sizepolicy import *

class Ui_MainwindowAdapter(QMainWindow, Ui_MainWindow):
    def __init__(self,*args, **kwargs):
        super(Ui_MainwindowAdapter,self).__init__(*args, **kwargs)
        self.setupUi(self)
        
        # self.pushButton_2.setMaximumSize(500,100)
        # self.pushButton_2.setMinimumSize(1,1)
        # self.pushButton.setMinimumSize(1,1)
        
        # self.setFixedSize(500,400)
        # self.setMinimumSize(100, 200)
        # self.setMaximumSize(800, 1000)
        
        print("self.geometry = {}".format(self.geometry()))
        # self.setGeometry(QRect(0,0,100,200))
        print("after set geometry self.geometry = {}".format(self.geometry()))
        
        # self.setMinimumSize(1,1)
        print("self.minimumSizeHint = {}".format(self.minimumSizeHint()))
        print("self.sizeHint = {}".format(self.sizeHint()))
        print("self.minimumSize = {}".format(self.minimumSize()))

    
        # self.setWindowFlag(QtCore.Qt.WindowCloseButtonHint | QtCore.Qt.WindowMinimizeButtonHint)
        # 没效果
        # self.setWindowFlag(QtCore.Qt.WindowType.WindowCloseButtonHint and QtCore.Qt.WindowType.WindowMaximizeButtonHint and QtCore.Qt.WindowType.WindowMinimizeButtonHint)
        # 有效果
        # self.setWindowFlag(Qt.FramelessWindowHint)
    
        self.pushButton.clicked.connect(self.print_sizehint)
        
    def print_sizehint(self):
        print("pushbutton-------------")
        print(self.pushButton.sizeHint())
        print(self.pushButton.minimumSizeHint())
        print(self.pushButton.minimumSize())
        print(self.pushButton.maximumSize())
    
        
        print("pushbtn_maxsize {}".format(self.pushButton_2.maximumSize()))
        
        print(self.centralwidget.sizeHint())
 

if __name__ == "__main__":
    app = QApplication(sys.argv)
    app.setApplicationName("test")
    window = Ui_MainwindowAdapter()
    window.show()
    sys.exit(app.exec_())