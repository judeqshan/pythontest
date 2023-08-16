# from PyQt5.QtCore import *
# from PyQt5.QtGui import *
# from PyQt5.QtWidgets import *
# from PyQt5.QtWidgets import QApplication

# import sys

# class PictureLabel(QLabel):

#     pictureClicked = pyqtSignal(str) # can be other types (list, dict, object...)

#     def __init__(self, image, parent=None):
#         super(PictureLabel, self).__init__(parent)        
#         self.setPixmap(QPixmap("input1.jpg"))

#     def mousePressEvent(self, event):
    
#         self.pictureClicked.emit("emit the signal")


# class Main(QWidget):


#     def __init__(self, parent=None):
#         super(Main, self).__init__(parent)

#         self.layout  = QVBoxLayout(self)

#         # picture = PictureLabel("input1.jpg", self)
#         # picture.pictureClicked.connect(self.anotherSlot)

#         picture = QLabel()
#         picture.setPixmap(QPixmap("input1.jpg"))
        
#         self.layout.addWidget(picture)
#         self.layout.addWidget(QLabel("click on the picture"))

#     def anotherSlot(self, passed):
#         print("now I'm in Main.anotherSlot")




# a = QApplication([])
# m = Main()
# m.show()
# sys.exit(a.exec_())

import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel
from PyQt5.QtGui import QIcon, QPixmap
import os

class App(QWidget):

    def __init__(self):
        super().__init__()
        self.title = 'PyQt5 image - pythonspot.com'
        self.left = 100
        self.top = 100
        self.width = 640
        self.height = 480
        self.initUI()
    
    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)
    
        # Create widget
        label = QLabel(self)
        # label.setGeometry(0,250,500,210)
        label.setText("testetserserserserserse")
        # pixmap = QPixmap("D:\\workspace\\pythontest\\pythontest\\run.jpg")
        url = os.path.dirname(os.path.abspath(__file__))
        p = url + "\\" + "run.jpg"
        p = "pic/input1.jpg"
        print(p)
        pixmap = QPixmap(p)
        label.setPixmap(pixmap)
        self.resize(pixmap.width(),pixmap.height())
        
        self.show()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec_())


# import sys
# from PyQt5.QtWidgets import QApplication,QWidget,QLabel,QPushButton
# from PyQt5.QtGui import QPixmap

# class MyClass(QWidget):
#     def __init__(self):
#         super().__init__()
#         self.initUI()

#     def initUI(self):
#         self.setWindowTitle("刘金玉编程")
#         self.setGeometry(300,100,400,300)
#         self.lbl=QLabel("图片",self)
#         self.pm=QPixmap("D:\\workspace\\pythontest\\pythontest\\input1.jpg")
#         self.lbl.setPixmap(self.pm)
#         self.lbl.resize(300,200)
#         self.lbl.setScaledContents(True)

#         #移除按钮
#         btn1=QPushButton("移除图片",self)
#         btn1.clicked.connect(self.myRemovePic)
#         btn1.move(0,220)
#         #增加按钮
#         btn2=QPushButton("增加图片",self)
#         btn2.clicked.connect(self.myAddPic)
#         btn2.move(0,250)
#         self.show()
#     def myRemovePic(self):
#         self.lbl.setPixmap(QPixmap(""))
#     def myAddPic(self):
#         print("addddddddddddddd")
#         self.lbl.setPixmap(self.pm)
# if __name__=="__main__":
#     app=QApplication(sys.argv)
#     mc=MyClass()
#     app.exec_()