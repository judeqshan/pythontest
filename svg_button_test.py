from PyQt5.QtWidgets import QWidget, QApplication, QHBoxLayout

from pyqt_svg_button.svgButton import SvgButton


class SvgButtonExample(QWidget):
    def __init__(self):
        super().__init__()
        self.__initUi()

    def __initUi(self):
        newButton = SvgButton()
        # newButton.setIcon('nesvgw.svg')

        openButton = SvgButton()
        openButton.setIcon('svg.svg')

        saveButton = SvgButton()
        saveButton.setIcon('save.svg')

        lay = QHBoxLayout()
        lay.addWidget(newButton)
        # lay.addWidget(openButton)
        # lay.addWidget(saveButton)

        self.setLayout(lay)


if __name__ == "__main__":
    import sys

    app = QApplication(sys.argv)
    ex = SvgButtonExample()
    ex.show()
    sys.exit(app.exec_())