import sys
from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5.QtGui import QPainter, QColor, QFont
from PyQt5.QtCore import Qt

class DrawingWindow(QWidget):
    def __init__(self, parent=None):
        super(DrawingWindow, self).__init__(parent)
        self.setWindowTitle("在窗口中绘制文字")
        self.resize(300, 200)
        self.text = "欢迎学习 PyQt5"

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.begin(self)
        # 自定义绘制方法
        self.drawText(event, painter)
        painter.end()

    def drawText(self, event, qp):
        # 设置画笔颜色
        qp.setPen(QColor(168, 35, 5))
        # 设置字体
        qp.setFont(QFont('SimSun', 20))
        # 绘制文字
        qp.drawText(event.rect(), Qt.AlignCenter, self.text)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = DrawingWindow()
    win.show()
    sys.exit(app.exec_())

        
