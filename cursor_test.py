# -*- coding: UTF-8 -*-
from PyQt5.Qt import *
import sys

# 创建一个应用
app = QApplication(sys.argv)
print(sys.argv)

# 创建一个QWidget类的窗口
window = QWidget()
window.setWindowTitle("鼠标操作")  # 标题
window.resize(500, 500)  # 窗口的大小
window.move(400, 200)  # 窗口初次显示的位置

# 自定义鼠标的样式
window.setCursor(Qt.OpenHandCursor)

window.show()  # 显示窗口，不然啥也没有

sys.exit(app.exec_())
