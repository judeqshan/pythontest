import sys
from PyQt5.QtWidgets import *


class MyWindow(QWidget):

    def __init__(self):
        super().__init__()

        self.setWindowTitle('PyQt5 弹出窗口')
        self.resize(400, 300)
        # 加了self为全局布局，没加为局部布局
        h1 = QHBoxLayout(self)
        btn = QPushButton('弹出窗口')
        btn.clicked.connect(self.do_btn)
        h1.addWidget(btn)

    def do_btn(self, event):  # 输入：整数
        # 后面四个数字的作用依次是 初始值 最小值 最大值 步幅
        # 1为默认选中选项目，True/False 列表框是否可编辑。 
        items = ["Spring", "Summer", "Fall", "Winter"]
        value, ok = QInputDialog.getItem(self, "输入框标题", "这是提示信息\n\n请选择季节:", items, 1, True)
        print(value)

        # value, ok = QInputDialog.getInt(self, "输入框标题", "这是提示信息\n\n请输入整数:", 37, -10000, 10000, 2)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = MyWindow()
    win.show()
    sys.exit(app.exec_())
