#!/usr/bin/env python
#-*- coding:utf-8 -*-
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import pyqtSignal, QTimer
from PyQt5.QtWidgets import *
import sys
 

class MyWindow(QtWidgets.QWidget):
    def __init__(self, parent=None):
        super(MyWindow, self).__init__(parent)

        self.region = QtGui.QRegion(QtCore.QRect(0, 0, 222, 222), QtGui.QRegion.Ellipse)
        self.setMask(self.region)

        self.palette = QtGui.QPalette()
        self.palette.setBrush(QtGui.QPalette.Background, QtGui.QColor('grey').darker(150))
        self.setPalette(self.palette)

        self.setWindowFlags(QtCore.Qt.FramelessWindowHint)

        self.label = QLabel(self)
        self.label.setText("A round widget!")
        self.label.setStyleSheet("QLabel { background-color : lightblue; color : white; }")
        self.label.setAlignment(QtCore.Qt.AlignCenter)

        self.layout = QHBoxLayout(self)
        self.layout.addWidget(self.label)

if __name__ == "__main__":
    import sys

    app = QApplication(sys.argv)
    window = MyWindow()
    window.show()
    sys.exit(app.exec_())