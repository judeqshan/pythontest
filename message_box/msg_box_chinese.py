# -*- coding: utf-8 -*-
"""
Created on Sat May  9 14:05:57 2020

@author: Giyn
"""

import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout, QMessageBox


class Simple_Window(QWidget):
    def __init__(self):
        super(Simple_Window, self).__init__() # 使用super函数可以实现子类使用父类的方法
        self.setWindowTitle("QMessageBox")
        self.resize(400, 200)
        self.button1 = QPushButton("Question", self) # self是指定的父类Simple_Window，表示QLabel属于Simple_Window窗口
        self.button2 = QPushButton("Information", self)
        
        # 连接信号和槽
        self.button1.clicked.connect(lambda: self.show_msg_box(self.button1)) # 槽函数带有参数，使用lambda表达式封装函数
        self.button2.clicked.connect(lambda: self.show_msg_box(self.button2))
        
        self.v_layout = QVBoxLayout() # 实例化一个QVBoxLayout对象
        self.v_layout.addWidget(self.button1)
        self.v_layout.addWidget(self.button2)
        
        self.setLayout(self.v_layout) # 调用窗口的setLayout方法将总布局设置为窗口的整体布局
        
    def show_msg_box(self, button):
        if button == self.button1:
            messageBox = QMessageBox(self)

            messageBox.setWinowIcon(QMessageBox.critical)

            messageBox.setWindowTitle('警告')

            messageBox.setText('向电网输出功率太大，请减小输出功率')

            messageBox.setStandardButtons(QMessageBox.Yes | QMessageBox.No)

            buttonY = messageBox.button(QMessageBox.Yes)

            buttonY.setText('设置')

            buttonN = messageBox.button(QMessageBox.No)

            buttonN.setText('忽略')

            messageBox.exec_()

            if messageBox.clickedButton() == buttonY:

                print('点击了yes')
        elif button == self.button2:
            QMessageBox.information(self, "Information", "I am an information.", QMessageBox.Ok)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Simple_Window()
    window.show()
    sys.exit(app.exec())
