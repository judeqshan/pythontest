import sys
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (
    QApplication, QTableView, QComboBox, QWidget,
    QVBoxLayout, QPushButton, QAbstractItemView
)
from PyQt5.QtGui import QStandardItemModel, QStandardItem
from PyQt5.QtWidgets import QStyledItemDelegate


class ComboBoxDelegate(QStyledItemDelegate):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.items = ['Option 1', 'Option 2', 'Option 3']
        # self.currentIndexChanged = lambda idx, value: None  # 定义一个空的槽函数

    def createEditor(self, parent, option, index):
        combo = QComboBox(parent)
        combo.addItems(self.items)
        # 连接信号到槽函数
        # combo.currentIndexChanged.connect(lambda value, idx=index: self.currentIndexChanged(idx, value))
        return combo

    def setEditorData(self, editor, index):
        value = index.model().data(index, Qt.EditRole)
        i = editor.findText(value)
        if i == -1:
            i = 0
        editor.setCurrentIndex(i)

    def setModelData(self, editor, model, index):
        model.setData(index, editor.currentText(), Qt.EditRole)

    def updateEditorGeometry(self, editor, option, index):
        editor.setGeometry(option.rect)


class CustomTableView(QTableView):
    def __init__(self, parent=None):
        super().__init__(parent)

    def showEvent(self, event):
        super().showEvent(event)
        # 在表格显示时打开所有需要显示下拉列表的单元格的编辑器
        self.openComboBoxEditors()

    def openComboBoxEditors(self):
        model = self.model()
        delegate = self.itemDelegateForColumn(1)
        if isinstance(delegate, ComboBoxDelegate):
            for row in range(model.rowCount()):
                index = model.index(row, 1)
                self.openPersistentEditor(index)


class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.model = QStandardItemModel(4, 2)
        self.model.setHeaderData(0, Qt.Horizontal, "Name")
        self.model.setHeaderData(1, Qt.Horizontal, "Options")

        self.view = CustomTableView()
        self.view.setModel(self.model)
        self.view.setItemDelegateForColumn(1, ComboBoxDelegate(self.view))
        self.view.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.view.resizeColumnsToContents()

        layout = QVBoxLayout()
        layout.addWidget(self.view)

        button = QPushButton('Add Row')
        button.clicked.connect(self.addRow)
        layout.addWidget(button)

        self.setLayout(layout)
        self.setWindowTitle('ComboBox Delegate in QTableView')

    def addRow(self):
        row = self.model.rowCount()
        self.model.insertRow(row)
        self.model.setData(self.model.index(row, 0), f'Row {row + 1}')
        self.model.setData(self.model.index(row, 1), 'Initial Value')


if __name__ == '__main__':
    app = QApplication(sys.argv)
    win = MainWindow()
    win.show()
    sys.exit(app.exec_())