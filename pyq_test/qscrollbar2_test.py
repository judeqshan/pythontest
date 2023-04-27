import sys
import os
 
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import (QApplication, QWidget, QLabel, QScrollBar, 
                             QSpacerItem, QSizePolicy, QVBoxLayout, QHBoxLayout, QFormLayout)
 
class DemoScrollBar(QWidget):
    def __init__(self, parent=None):
        super(DemoScrollBar, self).__init__(parent)       
        
        # 设置窗口标题
        self.setWindowTitle("实战PyQt5: QScrollBar Demo!")      
        # 设置窗口大小
        self.resize(440, 300)
        
        self.disp_w = 100
        self.disp_h = 280
        self.pos_horz = 0
        self.pos_vert = 0
        
        self.pix = QPixmap(os.path.dirname(__file__) + "\qt_py.jpg")
        print(os.path.dirname(__file__) + "\qt_py.jpg")
        img_w = self.pix.width()
        img_h = self.pix.height()
        
        self.disp_img = QLabel(self)
        # self.disp_img.setFixedSize(self.disp_w, self.disp_h)
        
        vBar = QScrollBar(Qt.Vertical, self)
        vBar.setRange(0, img_h - self.disp_h)
        vBar.setFixedHeight(self.disp_h)
        vBar.valueChanged.connect(self.vertPosChanged)
        
        hBar = QScrollBar(Qt.Horizontal, self)
        hBar.setRange(0, img_w - self.disp_w)
        hBar.setFixedWidth(self.disp_w)
        hBar.valueChanged.connect(self.horzPosChanged)
        
        fLayout = QFormLayout(self)
        fLayout.setWidget(0, QFormLayout.LabelRole, self.disp_img)
        fLayout.setWidget(0, QFormLayout.FieldRole, vBar)
        fLayout.setWidget(1, QFormLayout.LabelRole, hBar)
        
        #初始化显示区域
        self.disp_img.setPixmap(self.pix.copy(self.pos_horz, self.pos_vert, self.disp_w, self.disp_h))
        
        self.setLayout(fLayout)
        
    def horzPosChanged(self, pos):
        print(pos)
        self.pos_horz = pos
        self.disp_img.setPixmap(self.pix.copy(self.pos_horz,  self.pos_vert, self.disp_w, self.disp_h))
    
    def vertPosChanged(self, pos):
        self.pos_vert = pos
        self.disp_img.setPixmap(self.pix.copy(self.pos_horz,  self.pos_vert, self.disp_w, self.disp_h))
        
        
if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = DemoScrollBar()
    window.show()
    sys.exit(app.exec()) 