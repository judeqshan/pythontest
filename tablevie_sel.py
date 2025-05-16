import sys
from PyQt5.QtWidgets import QApplication, QTableView, QVBoxLayout, QWidget, QPushButton, QMessageBox
from PyQt5.QtCore import Qt, QAbstractTableModel, QModelIndex, QItemSelectionModel
from PyQt5.QtGui import QStandardItemModel, QStandardItem

class MyTableModel(QStandardItemModel):
    def __init__(self, parent=None):
        super(MyTableModel, self).__init__(parent)
        self.setHorizontalHeaderLabels(["Column 1", "Column 2"])
        # 初始化一些数据
        for i in range(50):
            item1 = QStandardItem(f"Item {i}")
            item2 = QStandardItem(f"Item {i} Column 2")
            self.setItem(i, 0, item1)
            self.setItem(i, 1, item2)

class MyTableView(QTableView):
    def __init__(self, parent=None):
        super(MyTableView, self).__init__(parent)
        self.setSelectionBehavior(QTableView.SelectRows)  # 设置选择行为为整行选择
        self.setSelectionMode(QTableView.MultiSelection)  # 设置选择模式为多选
        self.doubleClicked.connect(self.handleDoubleClick)

    def handleDoubleClick(self, index):
        # 当用户双击表格中的某个单元格时，获取选中的行
        selected_rows = self.selectionModel().selectedRows()
        if selected_rows:
            row_indices = [index.row() for index in selected_rows]
            self.printSelectedRows(row_indices)

    def printSelectedRows(self, row_indices):
        message = "Selected Rows:\n"
        for row in row_indices:
            message += f"Row {row}: "
            for col in range(self.model().columnCount()):
                index = self.model().index(row, col)
                message += f"{self.model().data(index)} "
            message += "\n"
        QMessageBox.information(self, "Selected Rows", message)

class MyWindow(QWidget):
    def __init__(self):
        super(MyWindow, self).__init__()
        self.initUI()

    def initUI(self):
        layout = QVBoxLayout()

        self.model = MyTableModel(self)
        self.view = MyTableView(self)
        self.view.setModel(self.model)

        button = QPushButton("Select Rows", self)
        button.clicked.connect(self.handleButtonClick)

        layout.addWidget(self.view)
        layout.addWidget(button)
        self.setLayout(layout)

    def handleButtonClick(self):
        selected_rows = self.view.selectionModel().selectedRows()
        if selected_rows:
            row_indices = [index.row() for index in selected_rows]
            self.view.printSelectedRows(row_indices)

if __name__ == '__main__':
    app = QApplication(sys.argv)

    window = MyWindow()
    window.resize(400, 300)
    window.show()

    sys.exit(app.exec_())
