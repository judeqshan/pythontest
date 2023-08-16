import sys
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPixmap, QColor, QPainterPath
from PyQt5.QtWidgets import QApplication, QGraphicsItem, QGraphicsLineItem, QGraphicsRectItem, QGraphicsEllipseItem, \
                            QGraphicsPixmapItem, QGraphicsTextItem, QGraphicsPathItem, QGraphicsScene, QGraphicsView


class Demo(QGraphicsView):
    def __init__(self):
        super(Demo, self).__init__()
        # 1
        self.resize(300, 300)

        # 2
        self.scene = QGraphicsScene()
        self.scene.setSceneRect(0, 0, 300, 300)

        # 3
        self.line = QGraphicsLineItem()
        self.line.setLine(100, 10, 200, 10)
        # self.line.setLine(QLineF(100, 10, 200, 10))

        # 4
        self.rect = QGraphicsRectItem()
        self.rect.setRect(100, 30, 100, 30)
        # self.rect.setRect(QRectF(100, 30, 100, 30))

        # 5
        self.ellipse = QGraphicsEllipseItem()
        self.ellipse.setRect(100, 80, 100, 20)
        # self.ellipse.setRect(QRectF(100, 80, 100, 20))

        # 6
        self.pic = QGraphicsPixmapItem()
        self.pic.setPixmap(QPixmap('D:\\workspace\\pythontest\\pythontest\\pic\\run.jpg').scaled(60, 60))
        self.pic.setFlags(QGraphicsItem.ItemIsSelectable | QGraphicsItem.ItemIsMovable)
        self.pic.setOffset(100, 120)
        # self.pic.setOffset(QPointF(100, 120))

        # 7
        self.text1 = QGraphicsTextItem()
        self.text1.setPlainText('Hello PyQt5')
        self.text1.setDefaultTextColor(QColor(66, 222, 88))
        self.text1.setPos(100, 180)

        self.text2 = QGraphicsTextItem()
        self.text2.setPlainText('Hello World')
        self.text2.setTextInteractionFlags(Qt.TextEditorInteraction)
        self.text2.setPos(100, 200)

        self.text3 = QGraphicsTextItem()
        self.text3.setHtml('<a href="https://baidu.com">百度</a>')
        self.text3.setOpenExternalLinks(True)
        self.text3.setTextInteractionFlags(Qt.TextBrowserInteraction)
        self.text3.setPos(100, 220)

        # 8
        self.path = QGraphicsPathItem()

        self.tri_path = QPainterPath()
        self.tri_path.moveTo(100, 250)
        self.tri_path.lineTo(130, 290)
        self.tri_path.lineTo(100, 290)
        self.tri_path.lineTo(100, 250)
        self.tri_path.closeSubpath()

        self.path.setPath(self.tri_path)

        # 9
        self.scene.addItem(self.line)
        self.scene.addItem(self.rect)
        self.scene.addItem(self.ellipse)
        self.scene.addItem(self.pic)
        self.scene.addItem(self.text1)
        self.scene.addItem(self.text2)
        self.scene.addItem(self.text3)
        self.scene.addItem(self.path)

        # 10
        self.setScene(self.scene)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    demo = Demo()
    demo.show()
    sys.exit(app.exec_())