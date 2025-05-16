import sys
from PyQt5.QtWidgets import QApplication, QTableView, QPushButton, QVBoxLayout, QWidget, QFileDialog
from PyQt5.QtCore import Qt, QAbstractTableModel, QModelIndex, pyqtSignal
from PyQt5.QtGui import QStandardItemModel, QStandardItem

class FileSelectTableModel(QAbstractTableModel):
    fileSelected = pyqtSignal(str)

    def __init__(self, parent=None):
        super(FileSelectTableModel, self).__init__(parent)
        self.files = []

    def rowCount(self, parent=QModelIndex()):
        return len(self.files)

    def columnCount(self, parent=QModelIndex()):
        return 2  # 两列：文件路径和按钮

    def data(self, index, role=Qt.DisplayRole):
        if not index.isValid():
            return None
        if role == Qt.DisplayRole:
            row = index.row()
            col = index.column()
            if col == 0:  # 文件路径列
                return self.files[row][0] if self.files else ''
            elif col == 1:  # 按钮列
                return ''  # 按钮列不显示任何文本
        return None

    def flags(self, index):
        if not index.isValid():
            return Qt.NoItemFlags
        if index.column() == 1:  # 按钮列可以触发事件
            return Qt.ItemIsEnabled | Qt.ItemIsSelectable | Qt.ItemIsUserCheckable
        return Qt.ItemIsEditable | Qt.ItemIsEnabled | Qt.ItemIsSelectable

    def setData(self, index, value, role=Qt.EditRole):
        if role == Qt.EditRole:
            row = index.row()
            col = index.column()
            if col == 0:  # 文件路径列
                self.files[row] = (value, QPushButton("Select File"))
                self.dataChanged.emit(index, index)
                return True
        return False

    def headerData(self, section, orientation, role=Qt.DisplayRole):
        if role == Qt.DisplayRole:
            if orientation == Qt.Horizontal:
                if section == 0:
                    return "File Path"
                elif section == 1:
                    return "Action"
        return None

    def openFile(self, index):
        options = QFileDialog.Options()
        file_name, _ = QFileDialog.getOpenFileName(None, "Select File", "", "All Files (*);;Text Files (*.txt)", options=options)
        if file_name:
            row = index.row()
            self.files[row] = (file_name, QPushButton("Select File"))
            self.fileSelected.emit(file_name)
            self.dataChanged.emit(index.sibling(row, 0), index.sibling(row, 0))

class FileSelectView(QWidget):
    def __init__(self):
        super(FileSelectView, self).__init__()
        self.initUI()

    def initUI(self):
        layout = QVBoxLayout()

        self.model = FileSelectTableModel(self)
        self.view = QTableView()
        self.view.setModel(self.model)

        # 连接信号槽
        self.view.clicked.connect(self.onCellClicked)

        layout.addWidget(self.view)
        self.setLayout(layout)

    def onCellClicked(self, index):
        if index.column() == 1:  # 只有当点击按钮列时才处理
            self.model.openFile(index)

if __name__ == '__main__':
    app = QApplication(sys.argv)

    window = FileSelectView()   
    window.resize(400, 200)
    window.show()

    sys.exit(app.exec_())
