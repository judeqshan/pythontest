import sys
from PyQt5.QtWidgets import QApplication, QGraphicsScene, QGraphicsView, QGraphicsLineItem, QGraphicsEllipseItem, QGraphicsTextItem
from PyQt5.QtCore import Qt, QPointF
from PyQt5.QtGui import QPainter


class MosfetDrawer(QGraphicsView):
    def __init__(self):
        super().__init__()
        self.scene = QGraphicsScene()
        self.setScene(self.scene)
        self.scene.setSceneRect(-200, -100, 400, 200)  # Set scene size
        self.scale(1.5, 1.5)  # Scale the view
        self.setRenderHint(QPainter.Antialiasing)  # Enable antialiasing

        # Draw the various parts of the MOSFET
        self.drawMosfet()

    def drawMosfet(self):
        # Gate
        gate_line = QGraphicsLineItem(QPointF(-100, 0), QPointF(-50, 0))
        gate_line.setPen(Qt.black)
        self.scene.addItem(gate_line)

        # Oxide layer of the gate
        oxide_line = QGraphicsLineItem(QPointF(-50, -20), QPointF(-50, 20))
        oxide_line.setPen(Qt.black)
        self.scene.addItem(oxide_line)

        # Source and Drain
        source_line = QGraphicsLineItem(QPointF(0, 50), QPointF(0, -50))
        source_line.setPen(Qt.black)
        self.scene.addItem(source_line)

        drain_line = QGraphicsLineItem(QPointF(100, 50), QPointF(100, -50))
        drain_line.setPen(Qt.black)
        self.scene.addItem(drain_line)

        # Body
        body_line = QGraphicsLineItem(QPointF(-50, 0), QPointF(0, 0))
        body_line.setPen(Qt.black)
        self.scene.addItem(body_line)

        # Body contact
        body_contact = QGraphicsEllipseItem(-40, -5, 10, 10)
        body_contact.setBrush(Qt.black)
        self.scene.addItem(body_contact)

        # Text labels
        gate_text = QGraphicsTextItem("G")
        gate_text.setPos(-75, 10)
        self.scene.addItem(gate_text)

        source_text = QGraphicsTextItem("S")
        source_text.setPos(15, 45)
        self.scene.addItem(source_text)

        drain_text = QGraphicsTextItem("D")
        drain_text.setPos(115, 45)
        self.scene.addItem(drain_text)

        # Body contact label
        body_contact_text = QGraphicsTextItem("B")
        body_contact_text.setPos(-35, -10)
        self.scene.addItem(body_contact_text)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    mosfet_view = MosfetDrawer()
    mosfet_view.show()
    sys.exit(app.exec_())