from PyQt5.QtWidgets import QApplication,QWidget,QAbstractItemView
from PyQt5.QtCore import Qt, pyqtSlot, QObject, QEvent
import sys
from ui_Widget import Ui_Widget

class QmyWidget(QWidget):
    def __init__(self,parent = None):
        super().__init__(parent)
        self.ui = Ui_Widget()
        self.ui.setupUi(self)
        self.ui.listSource.installEventFilter(self)
        self.ui.listWidget.installEventFilter(self)
        self.ui.treeWidget.installEventFilter(self)
        self.ui.tableWidget.installEventFilter(self)

        self.ui.listSource.setAcceptDrops(True)#设置可放置
        self.ui.listSource.setDragDropMode(QAbstractItemView.DragDrop)#设置拖放模式(只允许拖/只允许放/都没有...)
        self.ui.listSource.setDragEnabled(True)#设置可拖动
        self.ui.listSource.setDefaultDropAction(Qt.CopyAction)#设置拖动后的模式(完全复制/移动/关联数据...)

        self.ui.listWidget.setAcceptDrops(True)  # 设置可放置
        self.ui.listWidget.setDragDropMode(QAbstractItemView.DragDrop)  # 设置拖放模式(只允许拖/只允许放/都没有...)
        self.ui.listWidget.setDragEnabled(True)  # 设置可拖动
        self.ui.listWidget.setDefaultDropAction(Qt.CopyAction)  # 设置拖动后的模式(完全复制/移动/关联数据...)

        self.ui.treeWidget.setAcceptDrops(True)  # 设置可放置
        self.ui.treeWidget.setDragDropMode(QAbstractItemView.DragDrop)  # 设置拖放模式(只允许拖/只允许放/都没有...)
        self.ui.treeWidget.setDragEnabled(True)  # 设置可拖动
        self.ui.treeWidget.setDefaultDropAction(Qt.CopyAction)  # 设置拖动后的模式(完全复制/移动/关联数据...)

        self.ui.tableWidget.setAcceptDrops(True)  # 设置可放置
        self.ui.tableWidget.setDragDropMode(QAbstractItemView.DragDrop)  # 设置拖放模式(只允许拖/只允许放/都没有...)
        self.ui.tableWidget.setDragEnabled(True)  # 设置可拖动
        self.ui.tableWidget.setDefaultDropAction(Qt.CopyAction)  # 设置拖动后的模式(完全复制/移动/关联数据...)

        self.__itemView:parent ==QAbstractItemView = None
        self.on_radio_Source_clicked()
    def __refreshToUI(self): #根据初始化的界面设定选项
        self.ui.chkBox_AcceptDrops.setChecked(self.__itemView.acceptDrops())
        self.ui.chkBox_DragEnabled.setChecked(self.__itemView.dragEnabled())

        self.ui.combo_Mode.setCurrentIndex(self.__itemView.dragDropMode())
        index = self.__getDropActionIndex(self.__itemView.defaultDropAction())
        self.ui.combo_DefaultAction.setCurrentIndex(index)
    def __getDropActionIndex(self,actionType):
        if actionType == Qt.CopyAction:
            return 0
        elif actionType == Qt.MoveAction:
            return 1
        elif actionType == Qt.LinkAction:
            return 2
        elif actionType == Qt.IgnoreAction:
            return 3
        else:
            return 0
    def __getDropActionType(self,index):
        if index ==0:
            return Qt.CopyAction
        elif index ==1:
            return Qt.MoveAction
        elif index ==2:
            return Qt.LinkAction
        elif index ==3:
            return Qt.IgnoreAction
        else:
            return Qt.CopyAction
    def eventFilter(self, watched: 'QObject', event: 'QEvent') -> bool:
        if event.type() ==QEvent.KeyPress and event.key() == Qt.Key_Delete:
            if watched == self.ui.listSource:
                self.ui.listSource.takeItem(self.ui.listSource.currentRow())
            elif watched == self.ui.listWidget:
                self.ui.listWidget.takeItem(self.ui.listWidget.currentRow())
            elif watched == self.ui.treeWidget:
                curItem = self.ui.treeWidget.currentItem()
                if curItem.parent() !=None:
                    parItem = curItem.parent()
                    parItem.removeChild(curItem)
                else:
                    index = self.ui.treeWidget.indexOfTopLevelItem(curItem)
                    self.ui.treeWidget.takeTopLevelItem(index)
            elif watched ==self.ui.tableWidget:
                self.ui.tableWidget.takeItem(self.ui.tableWidget.currentRow(),self.ui.tableWidget.currentColumn())
        return super().eventFilter(watched,event)

    @pyqtSlot()
    def on_radio_Source_clicked(self):
        self.__itemView = self.ui.listSource
        self.__refreshToUI()
    @pyqtSlot()
    def on_radio_List_clicked(self):
        self.__itemView = self.ui.listWidget
        self.__refreshToUI()

    @pyqtSlot()
    def on_radio_Tree_clicked(self):
        self.__itemView = self.ui.treeWidget
        self.__refreshToUI()

    @pyqtSlot()
    def on_radio_Table_clicked(self):
        self.__itemView = self.ui.tableWidget
        self.__refreshToUI()

    @pyqtSlot(bool)
    def on_chkBox_AcceptDrops_clicked(self,checked):
        self.__itemView.setAcceptDrops(checked)
    @pyqtSlot(bool)
    def on_chkBox_DragEnabled_clicked(self, checked):
        self.__itemView.setDragEnabled(checked)
        self.ui.combo_Mode.currentIndexChanged
    @pyqtSlot(int)
    def on_combo_Mode_currentIndexChanged(self,index):
        self.__itemView.setDragDropMode((QAbstractItemView.DragDropMode)(index))
    @pyqtSlot(int)
    def on_combo_DefaultAction_currentIndexChanged(self,index):
        self.__itemView.setDefaultDropAction(self.__getDropActionType(index))


if __name__ == '__main__':
    app = QApplication(sys.argv)
    form = QmyWidget()
    form.show()
    sys.exit(app.exec_())