import sys
 
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton
 
def onClick_Button():
    print('获取坐标:第一种')
    print("widget.x() = %d" % widget.x())
    print("widget.y() = %d" % widget.y())
    print("widget.width() = %d" % widget.width())
    print("widget.height() = %d" % widget.height())
 
    print('获取坐标:第二种')
    print("widget.geometry().x() = %d" % widget.geometry().x())
    print("widget.geometry().y() = %d" % widget.geometry().y())
    print("widget.geometry().width() = %d" % widget.geometry().width())
    print("widget.geometry().height() = %d" % widget.geometry().height())
 
    print('获取坐标:第3种')
    print("widget.frameGeometry().x() = %d" % widget.frameGeometry().x())
    print("widget.frameGeometry().y() = %d" % widget.frameGeometry().y())
    print("widget.frameGeometry().width() = %d" % widget.frameGeometry().width())
    print("widget.frameGeometry().height() = %d" % widget.frameGeometry().height())
 
app = QApplication(sys.argv)
widget = QWidget()
btn = QPushButton(widget)
btn.setText('按钮')
btn.move(25,42)
btn.clicked.connect(onClick_Button)
widget.resize(300,240)
widget.move(250,200)
widget.setWindowTitle('获取屏幕坐标系')
widget.show()
sys.exit(app.exec_())
 