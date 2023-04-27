import sys,os
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import Qt, QCoreApplication
from PyQt5.QtGui import QPixmap, QColor, QFont
from PyQt5.QtWidgets import (QApplication, QWidget, QPushButton, QStyle,
                             QWizard, QWizardPage, QVBoxLayout, QPlainTextEdit,
                             QLabel, QLineEdit)
 
class WizardPage1(QWizardPage):
    def __init__(self, parent=None):
        super(WizardPage1, self).__init__(parent)
        
        #中间窗口部分显示的内容
        vLayout = QVBoxLayout(self)
        showText = QPlainTextEdit(self)
        showText.setReadOnly(True)
        showText.appendPlainText('Qt 安装向导测试1\n你可以自由使用这些代码，但风险自负')
        vLayout.addWidget(showText)
        
        self.setLayout(vLayout)
        
        self.setTitle("<font color='white' size='8'>版权申明</font>")
        self.setSubTitle('显示版权信息')
        
class WizardPage2(QWizardPage):
    def __init__(self, parent=None):
        super(WizardPage2, self).__init__(parent)
        
        #中间窗口部分显示的内容
        vLayout = QVBoxLayout(self)
        title = QLabel('设置安装路径:')
        
        installPath = QLineEdit(self)
        installPath.setText(QApplication.applicationDirPath())
 
        vLayout.addWidget(title)
        vLayout.addWidget(installPath)
        
        self.setLayout(vLayout)
        
        self.setTitle("<font color='white' size='8'>安装路径</font>")
        self.setSubTitle('设置安装路径')
        
class WizardPage3(QWizardPage):
    def __init__(self, parent=None):
        super(WizardPage3, self).__init__(parent)
        
        #中间窗口部分显示的内容
        vLayout = QVBoxLayout(self)
        info = QLabel(self)
        info.setFont(QFont(info.font().family(), 16))
        info.setAlignment(Qt.AlignCenter)
        info.setText('软件安装成功')
        vLayout.addStretch()
        vLayout.addWidget(info)
        vLayout.addStretch()
        
        self.setLayout(vLayout)
        
        self.setTitle("<font color='white' size='8'>完成</font>")
        self.setSubTitle('完成安装')
        
class WizardTest(QWizard):
    def __init__(self, parent=None):
        super(WizardTest, self).__init__(parent)
        
        self.setPage(0, WizardPage1(self))
        self.setPage(1, WizardPage2(self))
        self.setPage(2, WizardPage3(self))
        
        #去掉帮助按钮
        self.setWindowFlags(self.windowFlags()&~Qt.WindowContextHelpButtonHint)
        
        #设置导航样式
        self.setWizardStyle(QWizard.ModernStyle)
        #设置导航窗口标题
        self.setWindowTitle('Qt 向导 测试')
        
        #去掉页面的一些按钮
        self.setOption(QWizard.NoBackButtonOnStartPage) #首页没有回退按钮
        self.setOption(QWizard.NoBackButtonOnLastPage)  #最后一页没有回退按钮
        self.setOption(QWizard.NoCancelButton)         #没有取消按钮
        
        #设置导航栏背景标题
        pix = QPixmap(640, 64)
        pix.fill(QColor(52, 104, 192))
        self.setPixmap(QWizard.BannerPixmap, pix)
        
        #设置标题栏图标
        pix = QPixmap(os.path.dirname(__file__) + "/python.png")
        self.setPixmap(QWizard.LogoPixmap, pix.scaled(48,48))
        
        #设置页面主标题显示格式
        self.setTitleFormat(Qt.RichText)
        #设置子标题显示格式
        self.setSubTitleFormat(Qt.RichText)
        
        #设置按钮的显示名称
        self.setButtonText(QWizard.NextButton, '下一步')
        self.setButtonText(QWizard.BackButton, '上一步')
        self.setButtonText(QWizard.FinishButton, '完成')
        
class DemoWizard(QWidget):
    def __init__(self, parent=None):
        super(DemoWizard, self).__init__(parent)       
        
        # 设置窗口标题
        self.setWindowTitle('实战PyQt5: QWizard Demo!')      
        # 设置窗口大小
        self.resize(360, 120)
        
        self.initUi()
        
    def initUi(self):
        vLayout = QVBoxLayout(self)
        btnTest = QPushButton('向导对话框测试',self)
        btnTest.clicked.connect(self.onButtonTest)
        vLayout.addWidget(btnTest)
        self.setLayout(vLayout)
          
    def onButtonTest(self):
        dlg = WizardTest(self)
        dlg.exec()
    
if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = DemoWizard()
    window.show()
    sys.exit(app.exec())