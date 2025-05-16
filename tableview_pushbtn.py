import sys
from PyQt5.QtWidgets import QApplication, QTableView, QPushButton, QVBoxLayout, QWidget, QFileDialog
from PyQt5.QtCore import Qt, QModelIndex
from PyQt5.QtGui import QStandardItemModel, QStandardItem
from PyQt5.QtWidgets import QStyledItemDelegate, QStyle, QStyleOptionButton
from PyQt5 import QtWidgets



class ButtonDelegate(QStyledItemDelegate):
    buttonClicked = pyqtSignal(QModelIndex)  # 定义一个信号

    def __init__(self, parent=None):
        super(ButtonDelegate, self).__init__(parent)

    def paint(self, painter, option, index):
        if not index.isValid():
            return
        
        # 创建一个按钮选项对象
        opt = QStyleOptionButton()
        opt.rect = option.rect
        opt.text = "Open"
        opt.state |= QStyle.State_Enabled | QStyle.State_Raised

        # 绘制按钮
        self.parent().style().drawControl(QStyle.CE_PushButton, opt, painter)

    def editorEvent(self, event, model, option, index):
        if event.type() == QEvent.Type.MouseButtonRelease and event.button() == Qt.MouseButton.LeftButton:
            # 如果点击事件发生在按钮的区域内
            opt = QStyleOptionButton()
            opt.rect = option.rect
            hitRect = self.parent().style().subElementRect(QStyle.SE_PushButtonContents, opt)
            if hitRect.contains(event.pos()):
                # 发射信号
                self.buttonClicked.emit(index)
                return True
        return False

    def sizeHint(self, option, index):
        # 返回一个合适的大小提示
        opt = QStyleOptionButton()
        opt.text = "Open"
        return self.parent().style().sizeFromContents(QStyle.ContentsType.CT_PushButton, opt, option.rect.size(), self.parent())

class MyWindow(QWidget):
    def __init__(self):
        super(MyWindow, self).__init__()
        self.setupUi()

    def setupUi(self):
        self.model = QStandardItemModel(4, 2, self)  # 4行2列
        self.tableView = QTableView()
        self.tableView.setModel(self.model)

        # 使用自定义的委托
        delegate = ButtonDelegate(self.tableView)
        self.tableView.setItemDelegateForColumn(1, delegate)

        # 连接信号到槽函数
        delegate.buttonClicked.connect(self.openFile)

        layout = QVBoxLayout()
        layout.addWidget(self.tableView)
        self.setLayout(layout)

    def openFile(self, index):
        options = QFileDialog.Options()
        filePath, _ = QFileDialog.getOpenFileName(None, "Select File", "", "All Files (*);;Text Files (*.txt)", options=options)
        if filePath:
            self.model.setData(index, filePath, Qt.ItemDataRole.EditRole)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MyWindow()
    window.show()
    sys.exit(app.exec())