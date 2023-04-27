from PyQt5 import QtGui
from PyQt5.QtWidgets import QApplication, QWidget, QWizard, QVBoxLayout, QPushButton, QWizardPage
import sys


class Window(QWidget):
    def __init__(self):
        super().__init__()

        self.title = "PyQt5 Wizard"
        self.top = 200
        self.left = 500
        self.width = 400
        self.height = 300


        self.InitWindow()


    def InitWindow(self):
        self.setWindowIcon(QtGui.QIcon("icon.png"))
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)

        vbox= QVBoxLayout()

        button = QPushButton("Launch")
        button.clicked.connect(self.btn_clicked)

        vbox.addWidget(button)

        self.setLayout(vbox)

        # self.wizard = QWizard()
        self.wizard = QWizard()
        self.wizard.setWindowTitle("Launcher Page")

        self.show()



    def btn_clicked(self):

        self.wizard.open()

class WizardInit(QWizard):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Wizard")
        self.resize(500, 500)
        self.addPage(Page1())
        self.addPage(Page2())
        self.addPage(Page3())

class Page1(QWizardPage):
    def __init__(self):
        super().__init__()


class Page2(QWizardPage):
    def __init__(self):
        super().__init__()
        self.completeChanged.connect(self.next_btn)

    def next_btn(self):
        print("next")


class Page3(QWizardPage):
    def __init__(self):
        super().__init__()

App = QApplication(sys.argv)
window = Window()
sys.exit(App.exec_())