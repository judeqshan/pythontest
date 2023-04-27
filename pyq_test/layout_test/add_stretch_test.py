from tkinter import HORIZONTAL
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

import sys

class Form(QDialog):
    def __init__(self):
        super(Form, self).__init__()

        buttonLayout = QHBoxLayout()
        buttonLayout.addStretch()

        buttonLayout.addWidget(QPushButton("Yes"))
        buttonLayout.addWidget(QPushButton("No"))
        

        layout = QVBoxLayout()
        layout.addWidget(QLabel("Do you want to close this window without saving the data?"))
        layout.addLayout(buttonLayout)

        self.setLayout(layout)

app = QApplication(sys.argv)
form = Form()
form.show()
app.exec_()