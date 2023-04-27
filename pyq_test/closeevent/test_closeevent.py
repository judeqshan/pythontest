
from PyQt5.QtWidgets import (QApplication, QWidget, QPushButton, QLabel, QLineEdit, QMessageBox, QProgressDialog)
from PyQt5.QtCore import QRect
import sys
# 主窗口类
class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(1041, 860)
        self.pushButton = QPushButton(Form)
        self.pushButton.setGeometry(QRect(370, 80, 113, 32))
        self.pushButton.setObjectName("pushButton")
 
# 自定义窗口，继承QWidget
class MyWidget(QWidget):

    def closeEvent(self, event):
        result = QMessageBox.question(self, "标题", "亲，你确定想关闭我?别后悔！！！'_'", QMessageBox.Yes | QMessageBox.No)
        if(result == QMessageBox.Yes):
            event.accept()
            print("cccccccccccccccccccccc")
            # 通知服务器的代码省略，这里不是重点...
        else:
            event.ignore()
            print("ddddddddddddddddddddddddddddddd")

        return

if __name__ == "__main__":
    app = QApplication(sys.argv)
    parent = MyWidget()   # 自定义的QWidget窗口
    sub = Ui_Form()   # 主窗口
    sub.setupUi(parent)   # 子窗口继承自定义QWidget窗口
    parent.show()
    sys.exit(app.exec_())
