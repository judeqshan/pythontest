from PyQt5.QtWidgets import QLabel, QHBoxLayout, QApplication, QWidget

from pyqt_svg_label import SvgLabel





class IconTitleWidget(QWidget):

    def __init__(self):

        super().__init__()

        self.__initUi()



    def __initUi(self):

        iconLbl = SvgLabel()

        iconLbl.setSvgFile('ico/dark-notepad.svg')



        titleLbl = QLabel()

        titleLbl.setText('Dark Notepad')

        

        # get the point size of the titleLbl's font

        title_lbl_size = titleLbl.font().pointSize()



        # to match the iconLbl's size with titleLbl's font size (usually double size is appropriate)

        iconLbl.setFixedSize(title_lbl_size * 2, title_lbl_size * 2)



        lay = QHBoxLayout()

        lay.addWidget(iconLbl)

        lay.addWidget(titleLbl)



        self.setLayout(lay)





if __name__ == "__main__":

    import sys



    app = QApplication(sys.argv)

    ex = IconTitleWidget()

    ex.show()

    sys.exit(app.exec_())