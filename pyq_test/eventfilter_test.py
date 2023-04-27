import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (QApplication, QMainWindow, QWidget, 
                             QPushButton, QPlainTextEdit, QVBoxLayout,
                             QStatusBar)
 
class DemoEventFilter(QMainWindow):
    def __init__(self, parent=None):
        super(DemoEventFilter, self).__init__(parent)   
        
         # 设置窗口标题
        self.setWindowTitle('实战PyQt5: 事件过滤器演示')      
        # 设置窗口大小
        self.resize(400, 280)
      
        self.initUi()
        
    def initUi(self):
        #状态条
        self.sBar = QStatusBar(self)
        self.setStatusBar(self.sBar)
        
        mainWidget = QWidget()
        mainLayout = QVBoxLayout()
        
        self.filterInstalled = False
        self.btnSetFilter = QPushButton('安装事件过滤器')
        self.btnSetFilter.clicked.connect(self.onButtonSetFilter)
        
        self.textEditor = QPlainTextEdit()
        
        mainLayout.addWidget(self.btnSetFilter)
        mainLayout.addWidget(self.textEditor)
        
        mainWidget.setLayout(mainLayout)
        self.setCentralWidget(mainWidget)
    
    def onButtonSetFilter(self):
        if not self.filterInstalled:
            self.textEditor.installEventFilter(self)
            self.btnSetFilter.setText('卸载事件过滤器')
            self.filterInstalled = True
        else:
            self.textEditor.removeEventFilter(self)
            self.btnSetFilter.setText('安装事件过滤器')
            self.filterInstalled = False
    
    def eventFilter(self, watched, event):
        if(watched == self.textEditor and event.type() == event.KeyPress):
            self.sBar.showMessage('键盘事件被过滤', 500)
            return True
        return super(DemoEventFilter, self).eventFilter(watched, event)      
        
    
if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = DemoEventFilter()
    window.show()
    sys.exit(app.exec())