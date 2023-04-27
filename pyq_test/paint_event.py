import sys 
from PyQt5 import QtGui, QtWidgets 
from PyQt5.QtCore import Qt, QPoint 
 
class MyWidget(QtWidgets.QWidget): 
 
    def paintEvent(self, event): 
        qp = QtGui.QPainter() 
        qp.begin(self) 
        # self.resize(800,600)
        qp.setPen(QtGui.QColor(200,0,0)) 
        qp.drawText(20,20, "Text at fixed coordinates") 
        qp.drawText(event.rect(), Qt.AlignCenter, "Text centered in the drawing area") 
        print(event.rect())
        qp.setPen(QtGui.QPen(Qt.darkGreen, 4)) 
        qp.drawEllipse(QPoint(50,60),30,30) 
        qp.setPen(QtGui.QPen(Qt.blue, 2, join = Qt.MiterJoin)) 
        qp.drawRect(20,60,50,80) 
 
        qp.end() 
 
app = QtWidgets.QApplication(sys.argv) 
 
window = MyWidget() 
window.show() 
 
sys.exit(app.exec_())