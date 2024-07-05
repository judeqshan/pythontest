import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QLineEdit
from PyQt5.QtGui import  QRegularExpressionValidator, QRegExpValidator
from PyQt5.QtCore import QRegularExpression, QRegExp

class RegexLineEditExample(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Regex LineEdit Example')

        layout = QVBoxLayout()

        # Create a QLineEdit with a regex validator
        # regex = QRegularExpression("^[0-9]{3,3}$")  # Regular express ion pattern to allow only 3 digits
        regex = QRegExp("^[0-9]{3,3}$")  # Regular express ion pattern to allow only 3 digits
        regex.matchedLength =3
        # regex_validator = QRegularExpressionValidator(regex)
        regex_validator = QRegExpValidator(regex)
        line_edit = QLineEdit()
        line_edit1 = QLineEdit()
        line_edit.setValidator(regex_validator)

        layout.addWidget(line_edit)
        layout.addWidget(line_edit1)
        self.setLayout(layout)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = RegexLineEditExample()
    window.show()
    sys.exit(app.exec_())