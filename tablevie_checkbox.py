import random
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QAbstractItemView

class ItemDelegate(QtWidgets.QStyledItemDelegate):
    def createEditor(self, parent, options, index):
        column = index.column()
        if column == 0:
            return QtWidgets.QTextEdit(parent)
        elif column == 1:
            return QtWidgets.QComboBox(parent)
        elif column == 2:
            return QtWidgets.QSpinBox(parent)

    def setEditorData(self, editor, index):
        if isinstance(editor, QtWidgets.QTextEdit):
            editor.setText(index.data())
        elif isinstance(editor, QtWidgets.QComboBox):
            editor.addItems('Red Blue Green'.split())
            editor.setCurrentIndex(editor.findText(index.data()))
        elif isinstance(editor, QtWidgets.QSpinBox):
            editor.setValue(int(index.data()))

    def setModelData(self, editor, model, index):
        if isinstance(editor, QtWidgets.QTextEdit):
            model.setData(index, editor.toPlainText())
        elif isinstance(editor, QtWidgets.QComboBox):
            model.setData(index, editor.currentText())
        elif isinstance(editor, QtWidgets.QSpinBox):
            model.setData(index, editor.value())

class Window(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.table = QtWidgets.QTableWidget(5, 3)
        # self.table.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.table.setSelectionMode(QAbstractItemView.MultiSelection)
        self.table.setItemDelegate(ItemDelegate(self))
        layout = QtWidgets.QVBoxLayout(self)
        layout.addWidget(self.table)
        colours = 'Red Blue Green'.split()
        for row in range(5):
            for column in range(4):
                item = QtWidgets.QTableWidgetItem()
                if column == 1:
                    item.setData(QtCore.Qt.EditRole, random.choice(colours))
                elif column == 2:
                    item.setData(QtCore.Qt.EditRole, random.randint(0, 99))
                self.table.setItem(row, column, item)

if __name__ == '__main__':

    app = QtWidgets.QApplication(['Test'])
    window = Window()
    window.setGeometry(600, 100, 375, 225)
    window.show()
    app.exec()