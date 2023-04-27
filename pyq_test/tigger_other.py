from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

import sys

app = QApplication(sys.argv)

class mypb(QPushButton):
    def enterEvent(self, e):
        print('entered pushbutton!')

class w_test(QWidget):
    def __init__(self):
        super(w_test, self).__init__()

        self.pb_enter = mypb('ENTER ME', self)
        self.pb_enter.setText('ba')
        self.pb_test = QPushButton('trigger', self)
        self.pb_test.clicked.connect(self.f_trigger)
        self.init()

    def init(self):
        self.resize(500,300)
        self.pb_enter.resize(100,60)
        self.pb_enter.move(100, 100)
        self.pb_test.resize(100, 60)
        self.pb_test.move(300, 100)

    def enterEvent(self, e):
        print('entered widget!')

    def f_trigger(self):
        self.pb_enter.enterEvent(QEvent.Enter)
        print('I triggered another control\'s event!')

w = w_test()
w.show()
sys.exit(app.exec())