import sys
from PyQt5 import QtWidgets
from PyQt5 import QtCore
from PyQt5.QtGui import *

class CDemo(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()

        self.o_line_edit_0 = self._gen_line_edit_0()
        self.o_btn_0 = self._gen_btn_0()

        self.o_line_edit_1 = self._gen_line_edit_1()
        self.o_btn_1 = self._gen_btn_1()

        self.resize(300, 200)
        self.setLayout(self._gen_layout())

    def _gen_line_edit_0(self):
        _o_line_edit = QtWidgets.QLineEdit('line edit 0')
        _o_line_edit.setSelection(5, 9)
        return _o_line_edit

    def _gen_line_edit_1(self):
        _o_line_edit = QtWidgets.QLabel('line edit 1')
        #_o_palette = QPalette()      # 创建一个新调色板
        # _o_palette = _o_line_edit.palette() # 获取已有调色板，在已有调色板基础上修改
        # _o_palette.setColor(QPalette.Base           , QColor(255,0,0)) # 文本部件背景色
        # _o_palette.setColor(QPalette.WindowText           , QtCore.Qt.blue)   # 文本部件颜色
        # _o_palette.setColor(QPalette.Highlight      , QtCore.Qt.green)  # 文本部件选中的背景色
        # _o_palette.setColor(QPalette.HighlightedText, QtCore.Qt.red)    # 文本部件选中的文本颜色

        # _o_line_edit.setPalette(_o_palette)      # 为组件设置调色板
        # _o_line_edit.setAutoFillBackground(True) # 不加这句，则颜色不生效
        _o_line_edit.setText("<font color=#ffcc00>foo</font><font color=red>bar</font>")
        return _o_line_edit

    def _gen_btn_0(self):
        _o_btn = QtWidgets.QLabel('button 0')
        return _o_btn

    def _gen_btn_1(self):
        _o_btn = QtWidgets.QPushButton('button 1')

        #_o_palette = QPalette()
        _o_palette = _o_btn.palette() # 获取已有调色板，在已有调色板基础上修改
        _o_palette.setColor(QPalette.ButtonText, QtCore.Qt.blue)   # 按钮文本颜色
        #_o_palette.setColor(QPalette.Button   , QtCore.Qt.yellow) # 按钮背景色，不起效
        # 注意：QPushButton的背景色涉及样式表，所以不能通过QPalette修改.

        _o_btn.setPalette(_o_palette)      # 为组件设置调色板
        _o_btn.setAutoFillBackground(True) # 不加这句，则颜色不生效
        return _o_btn

    def _gen_layout(self):
        _o_layout_0 = QtWidgets.QHBoxLayout()
        _o_layout_0.addWidget(self.o_line_edit_0)
        _o_layout_0.addWidget(self.o_btn_0)
        _o_layout_0.addStretch(1)

        _o_layout_1 = QtWidgets.QHBoxLayout()
        _o_layout_1.addWidget(self.o_line_edit_1)
        _o_layout_1.addWidget(self.o_btn_1)
        _o_layout_1.addStretch(1)

        _o_layout_main = QtWidgets.QVBoxLayout()
        _o_layout_main.addLayout(_o_layout_0)
        _o_layout_main.addLayout(_o_layout_1)

        return _o_layout_main

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    win = CDemo()
    win.show()
    sys.exit(app.exec_())
