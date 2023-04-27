from  PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
import sys

from ui_draw_line import *

class Ui_MainwindowAdapter(QMainWindow, Ui_MainWindow):
    def __init__(self,*args, **kwargs):
        super(Ui_MainwindowAdapter,self).__init__(*args, **kwargs)
        self.setupUi(self)
        
        self.begin_point = QPoint()
        self.end_point = QPoint()

        self.pix = QPixmap(600, 600)            # 1
        self.pix.fill(Qt.white)
        
    def paintEvent(self, QPaintEvent):          # 2
        painter = QPainter(self.pix)
        painter.drawLine(self.begin_point, self.end_point)
        self.begin_point = self.end_point
        painter2 = QPainter(self)
        painter2.drawPixmap(0, 0, self.pix)   

    def mousePressEvent(self, QMouseEvent):
        if QMouseEvent.button() == Qt.LeftButton:
            self.begin_point = QMouseEvent.pos()
            self.end_point = self.begin_point
            self.update()

    def mouseMoveEvent(self, QMouseEvent):
        if QMouseEvent.buttons() == Qt.LeftButton:
            self.end_point = QMouseEvent.pos()
            self.update()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    app.setApplicationName("test")
    window = Ui_MainwindowAdapter()
    window.show()
    sys.exit(app.exec_())
    