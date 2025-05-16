import sys, os
from PyQt5 import QtCore, QtGui, QtWidgets

iconroot = os.path.dirname(__file__)

def create_image_layout():
        hlay = QtWidgets.QHBoxLayout()
        for icon_name in ("input1.jpg", 
                          "input1.jpg",
                          "input1.jpg",
                          "input1.jpg"):
        # for icon_name in ("images/fixed-fixed.png", 
        #                   "images/pinned-pinned.png",
        #                   "images/fixed-free.png",
        #                   "images/fixed-pinned.png"):

            label = QtWidgets.QLabel()
            pixmap = QtGui.QPixmap(os.path.join(iconroot, icon_name))
            label.resize(150, 150)
            label.setPixmap(pixmap.scaled(label.size(), QtCore.Qt.KeepAspectRatio))
            hlay.addWidget(label)
        return hlay

def create_EffLengthInfo_layout():
    hlay = QtWidgets.QHBoxLayout()
    for text in ('Ley = 1.0 L\nLec = 1.0 L',
                 'Ley = 0.699 L\nLec = 0.699 L',
                 'Ley = 2.0 L\nLec = 2.0 L',
                 'Ley = 0.5 L\nLec = 0.5 L'):
        label = QtWidgets.QLabel(text)
        hlay.addWidget(label)
    return hlay

def create_checkInfo_layout():
    hlay = QtWidgets.QHBoxLayout()
    for _ in range(3):
        checkbox = QtWidgets.QCheckBox()
        hlay.addWidget(checkbox, alignment=QtCore.Qt.AlignCenter)
    return hlay

class Grid(QtWidgets.QWidget):
    def __init__(self, parent=None):
        super(Grid, self).__init__(parent)

        image_lay = create_image_layout()
        efflengthinfo_lay = create_EffLengthInfo_layout()
        checkinfo_lay = create_checkInfo_layout()

        vlay = QtWidgets.QVBoxLayout(self)
        vlay.addLayout(image_lay)
        vlay.addLayout(efflengthinfo_lay)
        vlay.addLayout(checkinfo_lay)


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    im = Grid()
    im.show()
    sys.exit(app.exec_())