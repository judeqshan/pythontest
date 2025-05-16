import sys
from PyQt5.QtWidgets import QApplication, QTableView, QVBoxLayout, QWidget, QPushButton, QMessageBox
from PyQt5.QtCore import Qt, QModelIndex, QEvent
from PyQt5.QtGui import QStandardItemModel, QStandardItem

class MyTableView(QTableView):
    def __init__(self, parent=None):
        super(MyTableView, self).__init__(parent)
        self.setSelectionBehavior(QTableView.SelectRows)
        self.setSelectionMode(QTableView.SingleSelection)

        # 安装事件过滤器
        self.installEventFilter(self)

    def eventFilter(self, obj, event):
        print("111111111111111")
        if obj is self and event.type() == QEvent.MouseButtonRelease:
            print("222222222222222")
            if event.button() == Qt.LeftButton:
                index = self.indexAt(event.pos())
                if index.isValid():
                    row = index.row()
                    column = index.column()
                    print(f"Mouse released on row: {row}, column: {column}")
                    self.handleMouseRelease(index)
                else:
                    print("Mouse released outside of any item")
        return super().eventFilter(obj, event)

    def handleMouseRelease(self, index):
        # 在这里处理鼠标释放事件
        row = index.row()
        column = index.column()
        message = f"Row: {row}, Column: {column} clicked"
        QMessageBox.information(self, "Mouse Release", message)

class MainWindow(QWidget):
    def __init__(self):
        super(MainWindow, self).__init__()

        # 创建模型
        model = QStandardItemModel(4, 2, self)  # 4行2列
        for row in range(4):
            for column in range(2):
                item = QStandardItem(f"Item {row},{column}")
                model.setItem(row, column, item)

        # 创建并设置表格视图
        self.tableView = MyTableView(self)
        self.tableView.setModel(model)

        # 布局
        layout = QVBoxLayout()
        layout.addWidget(self.tableView)
        self.setLayout(layout)

if __name__ == '__main__':
    app = QApplication(sys.argv)

    main_window = MainWindow()
    main_window.show()

    sys.exit(app.exec_())
