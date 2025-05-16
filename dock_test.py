import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QDockWidget, QTextEdit, QLabel

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        # 创建第一个 QDockWidget
        self.dock1 = QDockWidget("Dock 1", self)
        self.dock1.setWidget(QTextEdit("This is Dock 1"))
        self.addDockWidget(Qt.LeftDockWidgetArea, self.dock1)

        # 创建第二个 QDockWidget
        self.dock2 = QDockWidget("Dock 2", self)
        self.dock2.setWidget(QTextEdit("This is Dock 2"))
        self.addDockWidget(Qt.LeftDockWidgetArea, self.dock2)

        # 将第一个 QDockWidget 置于顶层
        self.dock1.raise_()

        # 设置主窗口的标题和大小
        self.setWindowTitle("QDockWidget Example")
        self.resize(600, 400)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    mainWin = MainWindow()
    mainWin.show()
    sys.exit(app.exec_())