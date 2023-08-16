
# import cv2
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import pyqtSignal, QTimer
from PyQt5.QtWidgets import *
import sys
 
# 重写QtWidgets.QLabel mouseDoubleClickEvent鼠标双击事件，并绑定信号
class MyLabel(QtWidgets.QLabel):
    mouseDoubleClickSignal = pyqtSignal(object)
 
    def __init__(self, parent=None):
        super(MyLabel, self).__init__(parent)
        # 此处的img属性是要显示在label本身填充的图片对象
        self.img = None
 
    def mouseDoubleClickEvent(self, e):
        self.mouseDoubleClickSignal.emit(self)
 
# 主窗口
class MainWindow(QtWidgets.QWidget):
 
    def __init__(self):
        super(MainWindow, self).__init__()
        self.setupUi()
 
    def setupUi(self):
        self.setObjectName("Form")
        self.resize(600, 600)
        self.setMinimumSize(QtCore.QSize(600, 600))
        self.setMaximumSize(QtCore.QSize(600, 600))
        self.label = MyLabel(self)
        self.label.setMinimumSize(QtCore.QSize(600, 600))
        self.label.setMaximumSize(QtCore.QSize(600, 600))
        self.label.setObjectName("label")
        self.label.setText("testttttttttttttttt")
        # 信号槽连接显示子窗口的槽函数
        self.label.mouseDoubleClickSignal.connect(self.show_child_window)
        self.retranslateUi()
        QtCore.QMetaObject.connectSlotsByName(self)
 
    def retranslateUi(self):
        _translate = QtCore.QCoreApplication.translate
        self.setWindowTitle(_translate("Form", "MainWindow"))
    
    # 主窗口label控件设置图片
    def set_img(self, img):
        qImage = QtGui.QImage(img.data, img.shape[1], img.shape[0], QtGui.QImage.Format_BGR888)
        pixImage = QtGui.QPixmap.fromImage(qImage)
        # 给当前label对象的img属性赋值图像对象
        self.label.img = pixImage
        self.label.setPixmap(pixImage)
        self.label.setScaledContents(True)
    
    # 显示子窗口并给子窗口的label设置图像
    def show_child_window(self):
        self.child_window_ui = ChildWindow()
        self.child_window_ui.set_img(self.label.img)
        self.child_window_ui.show()
 
# 子窗口
class ChildWindow(QtWidgets.QWidget):
 
    def __init__(self):
        super(ChildWindow, self).__init__()
        self.setupUi()
 
    def setupUi(self):
        self.setObjectName("Form")
        self.resize(600, 600)
        self.setMinimumSize(QtCore.QSize(600, 600))
        self.setMaximumSize(QtCore.QSize(600, 600))
        self.label = MyLabel(self)
        self.label.setMinimumSize(QtCore.QSize(600, 600))
        self.label.setMaximumSize(QtCore.QSize(600, 600))
        self.label.setObjectName("label")
        # self.label.mouseDoubleClickSignal.connect(self.show_child_window)
        self.retranslateUi()
        QtCore.QMetaObject.connectSlotsByName(self)
 
    def retranslateUi(self):
        _translate = QtCore.QCoreApplication.translate
        self.setWindowTitle(_translate("Form", "ChildWindow"))
    
    # 子窗口label控件设置图片
    def set_img(self, img):
        qImage = QtGui.QImage(img.data, img.shape[1], img.shape[0], QtGui.QImage.Format_BGR888)
        pixImage = QtGui.QPixmap.fromImage(qImage)
        self.label.img = pixImage
        self.label.setPixmap(pixImage)
        self.label.setScaledContents(True)
        

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
