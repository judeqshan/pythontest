from email.charset import QP
from  PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
import sys

from qlinedit_test1 import *

from test_import import *
import qtawesome as qta

    

class Ui_MainwindowAdapter(QMainWindow, Ui_MainWindow):
    def __init__(self,*args, **kwargs):
        super(Ui_MainwindowAdapter,self).__init__(*args, **kwargs)
        self.setupUi(self)
    
        self.pushButton_read.clicked.connect(self.read)
        self.pushButton_set.clicked.connect(self.set)
        self.pushButton_setcombobox.clicked.connect(self.set_combo)
        self.comboBox.addItems(["neg","positive"])
        self.pushButton_size_hint.clicked.connect(self.print_sizehint)

        self.animation2 = qta.Pulse(self.pushButton_spin, autostart=False)
        pulse_icon = qta.icon('fa5s.spinner', color='green',
                              animation=self.animation2)
        self.pushButton_spin.setIcon(pulse_icon)

        self.pushButton_spin.clicked.connect(self.spining)
        self.is_sping = False

        
    
    def spining(self):
        if not self.is_sping:
            self.animation2.start()
            self.is_sping = True
        else:
            self.animation2.stop()
            self.is_sping = False
        
    def set(self):
        self.lineEdit.setText("11")

    def read(self):
        pass
        print(self.lineEdit.text())
        
    def set_combo(self):
        pass
        self.comboBox.setCurrentIndex()
        
    def print_sizehint(self):
        print(self.pushButton_size_hint.sizeHint())
        print(self.pushButton_read.sizeHint())
        print(self.label.sizeHint())
        ti = test_import()
        ti.test()

    def running(self):
        pass
        if not self.is_running:
            self.animation2.start()
            print("start")
            self.is_running = True
        else:
            self.is_running = False
            self.animation2.stop()
            print("stop")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    app.setApplicationName("test")
    window = Ui_MainwindowAdapter()
    window.show()
    sys.exit(app.exec_())
    