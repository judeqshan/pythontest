import sys
from PyQt5.QtWidgets import (
    QApplication, QTableView, QComboBox, QWidget, QVBoxLayout, QPushButton, QFileDialog,
    QAbstractItemView, QStyledItemDelegate, QCheckBox
)
from PyQt5.QtCore import Qt, QModelIndex
from PyQt5.QtGui import QStandardItemModel, QStandardItem
from PyQt5.QtWidgets import QStyleOptionButton, QStyle

class CheckBoxDelegate(QStyledItemDelegate):
    def createEditor(self, parent, option, index):
        # 不需要编辑器，因为我们不需要编辑复选框的内容
        return None

    def paint(self, painter, option, index):
        # 绘制复选框
        check_box_style_option = QStyleOptionButton()
        check_box_style_option.state |= QStyle.State_Enabled
        value = index.model().data(index, Qt.EditRole)
        if value:
            check_box_style_option.state |= QStyle.State_On
        else:
            check_box_style_option.state |= QStyle.State_Off
        check_box_style_option.rect = option.rect
        QApplication.style().drawControl(QStyle.CE_CheckBox, check_box_style_option, painter)

    def editorEvent(self, event, model, option, index):
        if event.type() == Qt.MouseButtonRelease or event.type() == Qt.KeyPress:
            if event.button() == Qt.LeftButton or event.key() == Qt.Key_Space:
                self.setModelData(None, model, index)
                return True
        return False

    def setModelData(self, editor, model, index):
        value = not bool(index.model().data(index, Qt.EditRole))
        model.setData(index, int(value), Qt.EditRole)

class ComboBoxDelegate(QStyledItemDelegate):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.items = ['Option 1', 'Option 2', 'Option 3']

    def createEditor(self, parent, option, index):
        combo = QComboBox(parent)
        combo.addItems(self.items)
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

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.model = QStandardItemModel(4, 3)
        self.model.setHeaderData(0, Qt.Horizontal, "Checkbox")
        self.model.setHeaderData(1, Qt.Horizontal, "Options")
        self.model.setHeaderData(2, Qt.Horizontal, "Other Column")

        self.view = QTableView()
        self.view.setModel(self.model)
        self.view.setItemDelegateForColumn(0, CheckBoxDelegate(self.view))
        self.view.setItemDelegateForColumn(1, ComboBoxDelegate(self.view))

        layout = QVBoxLayout()
        layout.addWidget(self.view)

        button = QPushButton('Add Row')
        button.clicked.connect(self.addRow)
        layout.addWidget(button)

        self.setLayout(layout)
        self.setWindowTitle('Custom Delegates in QTableView')

    def addRow(self):
        row = self.model.rowCount()
        self.model.insertRow(row)
        self.model.setData(self.model.index(row, 0), 0)  # 设置初始值为未选中状态
        self.model.setData(self.model.index(row, 1), 'Initial Value')
        self.model.setData(self.model.index(row, 2), '')

if __name__ == '__main__':
    app = QApplication(sys.argv)
    win = MainWindow()
    win.show()
    sys.exit(app.exec_())