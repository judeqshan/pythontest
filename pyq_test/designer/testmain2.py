from email.charset import QP
from  PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
import sys

from ui_draw_line import *

class PaintArea(QWidget):
    def __init__(self,*args, **kwargs):
        super(PaintArea,self).__init__(*args, **kwargs)
        self.paint_flag = 0
        
        self.pen1 = QPen()                      # 1
        self.pen1.setColor(Qt.red)
        self.pen1.setWidth(5)                   # 2

        self.pen2 = QPen()                      # 1
        self.pen2.setColor(Qt.blue)
        self.pen2.setWidth(5)                   # 2
        
        self.start = QPoint()
        self.end = QPoint()
        
        self.start2 = QPoint()
        self.end2 = QPoint()
    
    # def push(self):
    #     pass
    #     self.start = QPoint(100, 150)
    #     self.end = QPoint(600, 350)
    #     print("in start..............")
    #     self.update()
        
    def paintEvent(self, QPaintEvent):
        if self.paint_flag == 1:
            print("paint aear event")
            # print(self.start.x(), self.start.y(),self.end.x(),self.end.y())
            painter = QPainter(self)                # 6
            painter.setPen(self.pen1)
            
            res = painter.drawLine(self.start, self.end)  
            
            # painter2 = QPainter(self)                # 6
            # painter2.setPen(self.pen2)
            
            res = painter.drawLine(self.start2, self.end2)  
            
            # painter.drawRect(0, 0, 100, 100)
            
            print(res)
            print(self.width(),self.height())
            print("end in paint area")
            
        

class Ui_MainwindowAdapter(QMainWindow, Ui_MainWindow):
    def __init__(self,*args, **kwargs):
        super(Ui_MainwindowAdapter,self).__init__(*args, **kwargs)
        self.setupUi(self)
        self.pa = PaintArea(self.tab_1)
        
        # self.pa = PaintArea(self.tab_1)
        # self.pa = PaintArea()
        # self.gridLayout.addWidget(self.pa)
        
        # self.pen1 = QPen()                      # 1
        # self.pen1.setColor(Qt.red)
        # self.pen2 = QPen(Qt.SolidLine)
        # self.pen2.setWidth(36)                   # 2
    
        self.pushButton.clicked.connect(self.push)
        self.start = QPoint()
        self.end = QPoint()
    
    def push(self):
        pass
        # self.start = QPoint(100, 150)
        # self.end = QPoint(600, 350)
        self.pa.setFixedWidth(800)
        self.pa.setFixedHeight(800)
        
        self.pa.start = QPoint(20, 20)
        self.pa.end = QPoint(250, 210)
        
        self.pa.start2 = QPoint(0, 0)
        self.pa.end2 = QPoint(5000, 5000)
        
        self.pa.paint_flag = 1
        print("in start..............")
        self.pa.update()
        
    # def paintEvent(self, QPaintEvent):
    #     painter = QPainter(self)                # 6
    #     painter.setPen(self.pen1)
    #     painter.drawLine(self.start, self.end)  

if __name__ == "__main__":
    app = QApplication(sys.argv)
    app.setApplicationName("test")
    window = Ui_MainwindowAdapter()
    window.show()
    sys.exit(app.exec_())
    