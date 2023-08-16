from PyQt5.QtWidgets import QApplication,  QLabel  ,QWidget, QVBoxLayout 
from PyQt5.QtCore import Qt 
from PyQt5.QtGui import QPixmap ,QPalette
import sys  

from PyQt5.QtSvg import QSvgWidget, QSvgRenderer

svg_str = """<?xml version="1.0" encoding="UTF-8" standalone="no"?>
<svg width="300" height="300" viewBox="0 0 300 300" id="smile" version="1.1">
    <path
        style="fill:#ffaaaa"
        d="M 150,0 A 150,150 0 0 0 0,150 150,150 0 0 0 150,300 150,150 0 0 0 
            300,150 150,150 0 0 0 150,0 Z M 72,65 A 21,29.5 0 0 1 93,94.33 
            21,29.5 0 0 1 72,124 21,29.5 0 0 1 51,94.33 21,29.5 0 0 1 72,65 Z 
            m 156,0 a 21,29.5 0 0 1 21,29.5 21,29.5 0 0 1 -21,29.5 21,29.5 0 0 1 
            -21,-29.5 21,29.5 0 0 1 21,-29.5 z m -158.75,89.5 161.5,0 c 0,44.67 
            -36.125,80.75 -80.75,80.75 -44.67,0 -80.75,-36.125 -80.75,-80.75 z"
    />
</svg>
"""
# svg_bytes = bytearray(svg_str, encoding='utf-8')

# svgWidget = QSvgWidget()
# svgWidget.renderer().load(svg_bytes)
# svgWidget.setGeometry(100,100,300,300)
# svgWidget.show()
   
class WindowDemo(QWidget):  
    def __init__(self ):  
        super().__init__()
               
        label1 = QLabel(self)
        label2 = QLabel(self)
        label3 = QLabel(self)
        # label3 = QSvgWidget()
        # label3.renderer().load(svg_bytes)
        label4 = QLabel(self)
       
        #1
        label1.setText("这是一个文本标签。")
        label1.setAutoFillBackground(True) 
        palette = QPalette()   
        palette.setColor(QPalette.Window,Qt.blue)  
        label1.setPalette(palette) 
        label1.setAlignment( Qt.AlignCenter)
         
        label2.setText("<A href='https://blog.csdn.net/m0_38106923'>请关注公众号:美男子玩编程</a>")
       
        label3.setAlignment( Qt.AlignCenter)    
        label3.setToolTip('这是一个图片标签')
        label3.setPixmap( QPixmap("./4.jpg"))
        label4.setText("<A href='https://blog.csdn.net/m0_38106923'>欢迎关注不脱发的程序猿博客！</a>")
        label4.setAlignment( Qt.AlignRight)
        label4.setToolTip('这是一个超链接标签')
       
        #2
        vbox = QVBoxLayout()
        vbox.addWidget(label1)
        vbox.addStretch()
        vbox.addWidget(label2)
        vbox.addStretch()
        vbox.addWidget( label3 )
        vbox.addStretch()
        vbox.addWidget( label4)
       
        #3
        label2.setOpenExternalLinks(True)
        # 打开允许访问超链接,默认是不允许，需要使用 setOpenExternalLinks(True)允许浏览器访问超链接
        label4.setOpenExternalLinks(True)
        # 点击文本框绑定槽事件  
        label4.linkActivated.connect( link_clicked )
       
        # 划过文本框绑定槽事件       
        label2.linkHovered.connect( link_hovered )
        label1.setTextInteractionFlags( Qt.TextSelectableByMouse )
        self.setLayout(vbox)
        self.setWindowTitle("QLabel 例子")
       
def link_hovered():
    print("当鼠标滑过label-2标签时，触发事件。")
       
def link_clicked():
    print("当鼠标点击label-4标签时，触发事件。" )
 
if __name__ == "__main__":  
    app = QApplication(sys.argv)  
    win = WindowDemo()  
    win.show()  
    sys.exit(app.exec_())