from PyQt5.QtWidgets import QApplication,QLabel,QWidget,QVBoxLayout
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPixmap,QPalette
import sys

class WindowDemo(QWidget):
    def __init__(self):
        super(WindowDemo, self).__init__()

        #创建4个标签
        label1=QLabel(self)
        label2=QLabel(self)
        label3=QLabel(self)
        label4=QLabel(self)

        #初始化标签控件

        #setText():设置Qlabel的文本内容
        label1.setText('这是一个文本标签')
        #标签1的背景填充更改为True，否则无法显示背景
        label1.setAutoFillBackground(True)
        #实例化背景对象，进行相关背景颜色属性设置
        palette=QPalette()
        palette.setColor(QPalette.Window,Qt.blue)
        #标签1加载背景
        label1.setPalette(palette)
        #设置文本居中显示
        label1.setAlignment(Qt.AlignCenter)


        #设置标签2的显示文本
        label2.setText("<a href='#'>欢迎使用python gui应用</a>")
        #标签3居中
        label3.setAlignment(Qt.AlignCenter)
        #设置标签3的提示信息
        label3.setToolTip('这是一个图片标签')
        #标签3的背景图片加载
        label3.setPixmap(QPixmap("E:\pyqt5快速开发与实战\第四章\images\python.jpg"))

        #设置标签4的文本，含有超链接
        label4.setText("<A href='www.baidu.com'>欢迎百度</a>")
        #标签4靠右
        label4.setAlignment(Qt.AlignRight)
        #设置提示信息
        label4.setToolTip('这是一个超链接标签')
        
        
        label5 = QLabel()
        label5.setMinimumSize(300, 25)
        label5.setText('''<a style="font-family: 微软雅黑; color: #0000FF; font-size: 30pt;  text-decoration: none" href="www.qssoft.net.cn"> 访问网站 www.qssoft.net.cn</a>''')



        #在窗口布局中添加控件

        #垂直布局相关属性设置
        vbox=QVBoxLayout()
        #添加标签到垂直布局中
        vbox.addWidget(label1)
        #鼠标垂直拉伸不会改变高度
        vbox.addStretch()
        vbox.addWidget(label2)
        vbox.addStretch()
        vbox.addWidget(label3)
        vbox.addStretch()
        vbox.addWidget(label4)
        vbox.addStretch()
        vbox.addWidget(label5)
        vbox.addStretch()

        #允许label1控件访问超链接
        label1.setOpenExternalLinks(True)
        #默认不允许访问超链接，需要使用setOpenExternalLinks(True)允许

        #运行访问超链接
        label4.setOpenExternalLinks(True)
        #点击文本框绑定槽函数
        label4.linkActivated.connect(self.link_clicked)

        #滑过文本框绑定槽函数事件
        label2.linkHovered.connect(self.link_hovered)
        label1.setTextInteractionFlags(Qt.TextSelectableByMouse)

        #加载布局：前面设置好的垂直布局
        self.setLayout(vbox)
        #设置标题
        self.setWindowTitle('Qlabel例子')

    def link_hovered(self):
        print('当用鼠标点击label2标签时，触发事件')

    def link_clicked(self):
        print('当用鼠标点击label4标签时，触发事件')
if __name__ == '__main__':
    app=QApplication(sys.argv)
    win=WindowDemo()
    win.show()
    sys.exit(app.exec_())

