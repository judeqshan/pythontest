import sys
from PyQt5.QtWidgets import QApplication, QWidget, QMessageBox

app = QApplication(sys.argv)

widget = QWidget()

result = QMessageBox.question(widget, 'Message', "Do you want to close the application?", QMessageBox.Yes | QMessageBox.No, QMessageBox.No)

if result == QMessageBox.Yes:
    print('Yes clicked.')
else:
    print('No clicked.')

sys.exit(app.exec_())