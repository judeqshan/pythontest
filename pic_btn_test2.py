from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtWidgets import QApplication

import sys


class Stadium(QWidget):
    def __init__(self, pixmap, parent=None):
        QWidget.__init__(self, parent=parent)
        self.pixmap = pixmap
        self.pos = None
        self.setMouseTracking(True)

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.drawPixmap(self.rect(), self.pixmap)
        painter.setPen(QPen(Qt.red, 15, Qt.SolidLine))
        if self.pos:
            painter.drawEllipse(self.pos, 15, 15)

    def mouseMoveEvent(self, event):
        self.pos = event.pos()
        self.update()
        
class Widget(QWidget):
    def __init__(self, parent=None):
        QWidget.__init__(self, parent=parent)
        self.setLayout(QVBoxLayout())
        label = Stadium(QPixmap("youtube.png"))
        self.layout().addWidget(label)
        self.resize(640, 480)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = Widget()
    w.show()
    sys.exit(app.exec_())