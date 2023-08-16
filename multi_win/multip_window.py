# from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QLabel, QVBoxLayout, QWidget

# import sys


# class AnotherWindow(QWidget):
#     """
#     This "window" is a QWidget. If it has no parent, it
#     will appear as a free-floating window as we want.
#     """
#     def __init__(self, num):
#         super().__init__()
#         layout = QVBoxLayout()
#         self.label = QLabel(f"Another Window {num}")
#         layout.addWidget(self.label)
#         self.setLayout(layout)


# class MainWindow(QMainWindow):

#     def __init__(self):
#         super().__init__()
#         self.button = QPushButton("Push for Window")
#         self.button.clicked.connect(self.show_new_window)
#         self.setCentralWidget(self.button)
#         self.win_num=0
#         self.w = [0,0]

#     def show_new_window(self, checked):
#         self.w[self.win_num] = AnotherWindow(self.win_num)
#         self.w[self.win_num].show()
#         if self.win_num == 0:
#             self.win_num = self.win_num + 1
#         else:
#             self.win_num = 0


# app = QApplication(sys.argv)
# w = MainWindow()
# w.show()
# app.exec()


for iaa in range(0,9):
    print(iaa)