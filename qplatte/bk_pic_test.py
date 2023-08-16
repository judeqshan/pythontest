# from PyQt5.Qt import *
# import sys

# app = QApplication(sys.argv)

# w = QWidget()
# w.resize(210, 280)
# palette = QPalette()
# pix=QPixmap("D:\\workspace\\pythontest\\pythontest-main——copy\\input1.jpg")

# #pix = pix.scaled(w.width(),w.height())

# palette.setBrush(QPalette.Background,QBrush(pix))
# w.setPalette(palette)

# w.show()

# if __name__ == '__main__':
#     sys.exit(app.exec_())




import sys
from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5.QtGui import QPainter,QPixmap
from PyQt5.QtCore import Qt


class Winform(QWidget):
    def __init__(self, parent=None):
        super(Winform, self).__init__(parent)
        self.setWindowTitle("paintEvent设置背景颜色")

    def paintEvent(self, event):
        painter = QPainter(self)
        #todo 1 设置背景颜色
        # painter.setBrush(Qt.green)
        # painter.drawRect(self.rect())

        # #todo 2 设置背景图片，平铺到整个窗口，随着窗口改变而改变
        pixmap = QPixmap("D:\\workspace\\pythontest\\pythontest-main——copy\\input1.jpg")
        painter.drawPixmap(self.rect(), pixmap)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    form = Winform()
    form.show()
    sys.exit(app.exec_())
