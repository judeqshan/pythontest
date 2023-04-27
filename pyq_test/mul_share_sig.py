import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QDialog, QPushButton
from PyQt5.QtCore import QObject, Qt, pyqtSignal

# cls stand for class here.
class MySignal(QObject):
    """
    信号类
    """
    instance = None
    signal = pyqtSignal()

    @classmethod
    def my_signal(cls):
        if cls.instance:
            return cls.instance
        else:
            obj = cls()
            cls.instance = obj
            return cls.instance

    def em(self):
        self.signal.emit()

class MainWindow(QMainWindow):
    """
    主窗口类
    """
    Signal = MySignal.my_signal().signal

    def __init__(self, *args):
        super(MainWindow, self).__init__(*args)

        # 设置主窗口的标题及大小
        self.setWindowTitle('主窗口')
        self.resize(400, 300)

        # 创建按钮
        self.btn = QPushButton(self)
        self.btn.setText('弹出对话框')
        self.btn.move(50, 50)
        self.btn.clicked.connect(self.show_dialog)

        # 自定义信号绑定
        self.Signal.connect(self.test)

        self.dialog = Dialog()

    def show_dialog(self):
        self.dialog.show()
        self.dialog.exec()

    def test(self):
        self.btn.setText('我改变了')

class Dialog(QDialog):
    """
    对话框类
    """
    def __init__(self, *args):
        super(Dialog, self).__init__(*args)

        # 设置对话框的标题及大小
        self.setWindowTitle('对话框')
        self.resize(200, 200)
        self.setWindowModality(Qt.ApplicationModal)
        self.btn = QPushButton(self)
        self.btn.setText('改变主窗口按钮的名称')
        self.btn.move(50, 50)
        self.btn.clicked.connect(MySignal.my_signal().em)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    demo = MainWindow()
    demo.show()
    sys.exit(app.exec())
