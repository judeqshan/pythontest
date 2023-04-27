import sys
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPainter, QPen
from PyQt5.QtWidgets import QApplication, QWidget


class Demo(QWidget):
    def __init__(self):
        super(Demo, self).__init__()
        self.resize(600, 600)

        self.pen1 = QPen()                      # 1
        self.pen1.setColor(Qt.green)
        self.pen2 = QPen(Qt.SolidLine)
        self.pen2.setWidth(6)                   # 2
        # self.pen2.setWidthF(3.3)
        self.pen3 = QPen(Qt.DashLine)
        self.pen4 = QPen(Qt.DotLine)
        self.pen5 = QPen(Qt.DashDotLine)
        self.pen6 = QPen(Qt.DashDotDotLine)
        self.pen7 = QPen(Qt.CustomDashLine)     # 3
        self.pen7.setDashPattern([6, 2, 18, 2])

        self.pen8 = QPen(Qt.SolidLine)          # 4
        self.pen8.setWidth(6)
        self.pen8.setCapStyle(Qt.RoundCap)

        self.pen9 = QPen(Qt.SolidLine)          # 5
        self.pen9.setWidthF(6)
        self.pen9.setJoinStyle(Qt.MiterJoin)

    def paintEvent(self, QPaintEvent):
        painter = QPainter(self)                # 6
        painter.setPen(self.pen1)
        painter.drawLine(100, 10, 500, 10)      

        painter.setPen(self.pen2)
        painter.drawLine(100, 30, 500, 30)

        painter.setPen(self.pen3)
        painter.drawLine(100, 50, 500, 50)

        painter.setPen(self.pen4)
        painter.drawLine(100, 70, 500, 70)

        painter.setPen(self.pen5)
        painter.drawLine(100, 90, 500, 90)

        painter.setPen(self.pen6)
        painter.drawLine(100, 110, 500, 110)

        painter.setPen(self.pen7)
        painter.drawLine(100, 130, 500, 130)

        painter.setPen(self.pen8)
        painter.drawLine(100, 150, 500, 150)

        painter.setPen(self.pen2)
        painter.drawRect(100, 170, 400, 200)    # 7    

        painter.setPen(self.pen9)
        painter.drawRect(100, 390, 400, 200)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    demo = Demo()
    demo.show()
    sys.exit(app.exec_())