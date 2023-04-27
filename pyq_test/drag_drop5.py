import sys
import sys
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *


class TableView(QTableView):
    def __init__(self, parent=None):
        QTreeWidget.__init__(self, parent)
        self.setDragEnabled(True)
        self.setDropIndicatorShown(True)
        self.setDragDropMode(QAbstractItemView.DragDrop)
        self.setDragDropOverwriteMode(False)
        self.setSelectionBehavior(QAbstractItemView.SelectRows)

    def dragEnterEvent(self, event):
        event.accept()

    def dropEvent(self, event):
        if self.viewport().rect().contains(event.pos()):
            fake_model = QStandardItemModel()
            fake_model.dropMimeData(
                event.mimeData(), event.dropAction(), 0, 0, QModelIndex()
            )
            print("from:")
            for r in range(fake_model.rowCount()):
                for c in range(fake_model.columnCount()):
                    ix = fake_model.index(r, c)
                    print(ix.data())
            to_index = self.indexAt(event.pos())
            if to_index.isValid():
                print("to:", to_index.data())
        super(TableView, self).dropEvent(event)


class Dialog(QDialog):
    def __init__(self):
        super(Dialog, self).__init__()

        model = QStandardItemModel(self)
        for letter in "ABC":
            model.appendRow(QStandardItem(letter))

        table = TableView()
        table.setModel(model)

        lay = QVBoxLayout(self)
        lay.addWidget(table)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    ex = Dialog()
    ex.show()
    sys.exit(app.exec_())