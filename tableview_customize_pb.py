import sys
from PyQt5.QtWidgets import (
    QApplication, QTreeWidget, QTreeWidgetItem, QPushButton, QVBoxLayout, QWidget, 
    QFileDialog, QStyledItemDelegate, QStyle, QStyleOptionButton, QAbstractItemView
)
from PyQt5.QtCore import Qt, QModelIndex, QSize, QPoint, QRect
from PyQt5.QtGui import QStandardItemModel, QStandardItem, QPixmap, QColor, QPen

ScaleRole = Qt.UserRole + 1
expanderSize = 50

class TreeDelegate(QStyledItemDelegate):
    def __init__(self, parent=None):
        super(TreeDelegate, self).__init__(parent)
        self.pixmap_collapsed = QPixmap("collapsed.png")
        self.pixmap_collapsed_hover = QPixmap("collapsed_hover.png")
        self.pixmap_expanded = QPixmap("expanded.png")
        self.pixmap_expanded_hover = QPixmap("expanded_hover.png")

    def paint(self, painter, option, index):
        image = index.data(Qt.DecorationRole)
        scale = index.data(ScaleRole)
        name = index.data(Qt.DisplayRole)

        painter.save()
        rect = option.rect
        painter.setPen(QPen(QColor(43, 43, 43), 1))
        if option.state & QStyle.State_Selected:
            painter.setBrush(option.palette.highlight())
        else:
            painter.setBrush(index.data(Qt.BackgroundRole))
        painter.drawRect(rect)

        margin = 4
        image_scale = (rect.height() - margin * 2 + 1) * QSize(1, 1)
        if image is not None and not image.isNull():
            image = image.scaled(image_scale, Qt.KeepAspectRatio, Qt.SmoothTransformation)
            painter.drawPixmap(rect.topLeft() + QPoint(margin, margin), image)

        painter.setPen(QColor(255, 255, 255))
        font = painter.font()
        font.setPointSize(9)
        painter.setFont(font)
        painter.drawText(QRect(rect.topLeft() + QPoint(image_scale.width() + 3 * margin, 0), QSize(300, scale)),
                         Qt.AlignLeft | Qt.AlignVCenter, name)

        if index.model().hasChildren(index):
            if option.state & QStyle.State_Open:
                pixmap = self.pixmap_expanded_hover if option.state & QStyle.State_MouseOver else self.pixmap_expanded
            else:
                pixmap = self.pixmap_collapsed_hover if option.state & QStyle.State_MouseOver else self.pixmap_collapsed
            pixmap = pixmap.scaled(expanderSize * QSize(1, 1), Qt.KeepAspectRatio, Qt.SmoothTransformation)
            pos = rect.topRight() - QPoint(expanderSize + 10, int((expanderSize - scale) / 2))
            painter.drawPixmap(pos, pixmap)
        painter.restore()

class MyTreeItem(QTreeWidgetItem):
    def __init__(self, name, image, color, scale):
        super(MyTreeItem, self).__init__([name])
        self.setData(0, ScaleRole, scale)
        self.setData(0, Qt.BackgroundRole, color)
        self.setData(0, Qt.DecorationRole, image)

class MyTree(QTreeWidget):
    def __init__(self, parent=None):
        super(MyTree, self).__init__(parent)
        self.setMouseTracking(True)
        self.setHeaderHidden(True)
        self.setRootIsDecorated(False)
        self.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)

    def mousePressEvent(self, event):
        if not self.itemsExpandable(): return
        index = self.indexAt(event.pos())
        if not index.isValid(): return

        is_expanded = self.isExpanded(index)
        QAbstractItemView.mousePressEvent(self, event)
        self.setExpanded(index, is_expanded)

        if not self.model().hasChildren(index): return
        rect = self.visualRect(index)
        size = expanderSize
        scale = index.data(ScaleRole)
        pos = rect.topRight() - QPoint(size + 10, int((size - scale) / 2))
        r = QRect(pos, size * QSize(1, 1))
        if r.contains(event.pos()):
            self.setExpanded(index, not self.isExpanded(index))

def generate_tree():
    tree = MyTree()
    scale = 100
    delegate = TreeDelegate(tree)
    tree.setItemDelegate(delegate)

    for text in ["Aaaaaaa", "Bbbbbbb", "Ccccccc"]:
        item = MyTreeItem(text, QPixmap("image.png"), QColor(150, 150, 150), scale)
        item.setSizeHint(0, QSize(scale, scale))
        tree.addTopLevelItem(item)
        for child in ["Eeeeee", "Fffffff"]:
            childItem = MyTreeItem(child, QPixmap("image.png"), QColor(150, 150, 150), scale)
            childItem.setSizeHint(0, QSize(scale, scale))
            item.addChild(childItem)
    return tree

if __name__ == '__main__':
    app = QApplication(sys.argv)
    tree = generate_tree()    
    tree.show()
    sys.exit(app.exec_())
