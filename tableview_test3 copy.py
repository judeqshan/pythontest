import sys
from PyQt5.QtWidgets import (
    QApplication, QTableView, QWidget, QVBoxLayout, QPushButton, QHeaderView,
    QStyleOptionHeader, QStyle, QCheckBox, QHBoxLayout, QLabel,QStyleOptionButton
)
from PyQt5.QtCore import Qt, QModelIndex, pyqtSignal, QEvent
from PyQt5.QtGui import QStandardItemModel, QStandardItem, QPainter
from PyQt5.QtWidgets import QStyledItemDelegate

class HeaderWithCheckBox(QHeaderView):
    sectionClicked = pyqtSignal(int)

    def __init__(self, orientation, parent=None):
        super().__init__(orientation, parent)
        self._check_boxes = {}

    def paintSection(self, painter, rect, logicalIndex):
        super().paintSection(painter, rect, logicalIndex)
        if logicalIndex == 0:  # 只在第一列的表头显示复选框
            check_box = self._check_boxes.get(logicalIndex)
            if check_box is None:
                check_box = QCheckBox()
                check_box.stateChanged.connect(lambda state, idx=logicalIndex: self.onCheckBoxStateChanged(state, idx))
                self._check_boxes[logicalIndex] = check_box

            # option = QStyleOptionHeader()
            # self.initStyleOption(option)
            check_box_style_option = QStyleOptionButton()
            check_box_style_option.state |= QStyle.State_Enabled
            if check_box.isChecked():
                check_box_style_option.state |= QStyle.State_On
            else:
                check_box_style_option.state |= QStyle.State_Off
            check_box_style_option.rect = rect
            # QApplication.style().drawControl(QStyle.CE_Header, option, painter)
            QApplication.style().drawControl(QStyle.CE_CheckBox, check_box_style_option, painter)

    def onCheckBoxStateChanged(self, state, logicalIndex):
        # self.sectionClicked.emit(logicalIndex)
        if state == Qt.Checked:
            self.parent().model().setAllChecked(True)
        else:
            self.parent().model().setAllChecked(False)

    def mousePressEvent(self, event):
        logicalIndex = self.logicalIndexAt(event.pos())
        if logicalIndex == 0 and self._check_boxes.get(logicalIndex).geometry().contains(event.pos()):
            self._check_boxes[logicalIndex].toggle()
            self.sectionClicked.emit(logicalIndex)
            self.updateSection(0)
        else:
            super().mousePressEvent(event)

class CheckBoxDelegate(QStyledItemDelegate):
    def createEditor(self, parent, option, index):
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
        if event.type() == QEvent.MouseButtonRelease or event.type() == QEvent.KeyPress:
            if event.button() == Qt.LeftButton or event.key() == Qt.Key_Space:
                self.setModelData(None, model, index)
                return True
        return False

    def setModelData(self, editor, model, index):
        value = not bool(index.model().data(index, Qt.EditRole))
        model.setData(index, int(value), Qt.EditRole)

class MyStandardItemModel(QStandardItemModel):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._all_checked = False

    def setAllChecked(self, checked):
        self._all_checked = checked
        for row in range(self.rowCount()):
            index = self.index(row, 0)
            self.setData(index, int(checked), Qt.EditRole)

    def data(self, index, role=Qt.DisplayRole):
        if role == Qt.EditRole and index.column() == 0:
            # return int(self._all_checked or super().data(index, role))
            return int(self._all_checked)
        return super().data(index, role)

    def setData(self, index, value, role=Qt.EditRole):
        if role == Qt.EditRole and index.column() == 0:
            self._all_checked = value
            return super().setData(index, value, role)
        return super().setData(index, value, role)

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.model = MyStandardItemModel(4, 3)
        # self.model = QStandardItemModel(4, 3)
        self.model.setHeaderData(0, Qt.Horizontal, "Checkbox")
        self.model.setHeaderData(1, Qt.Horizontal, "Options")
        self.model.setHeaderData(2, Qt.Horizontal, "Other Column")

        self.view = QTableView()
        self.view.setModel(self.model)
        self.view.setItemDelegateForColumn(0, CheckBoxDelegate(self.view))
        self.view.horizontalHeader().setSectionResizeMode(0, QHeaderView.ResizeToContents)
        # self.view.horizontalHeader().sectionClicked.connect(self.toggleAllCheckboxes)
        self.view.setHorizontalHeader(HeaderWithCheckBox(Qt.Horizontal, self.view))

        layout = QVBoxLayout()
        layout.addWidget(self.view)

        button = QPushButton('Add Row')
        button.clicked.connect(self.addRow)
        layout.addWidget(button)

        self.setLayout(layout)
        self.setWindowTitle('Custom Delegates in QTableView')

    # def toggleAllCheckboxes(self, logicalIndex):
    #     if logicalIndex == 0:
    #         all_checked = not self.model._all_checked
    #         self.model.setAllChecked(all_checked)

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