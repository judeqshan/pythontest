import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QWidget
from PyQt5.QtGui import QScreen
from matplotlib.figure import Figure
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas

class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()

        # 创建一个 QWidget 作为主窗口的中心部件
        central_widget = QWidget(self)
        self.setCentralWidget(central_widget)

        # 创建一个垂直布局
        layout = QVBoxLayout(central_widget)

        # 创建一个 Figure 和 FigureCanvas
        self.figure = Figure()
        self.canvas = FigureCanvas(self.figure)

        # 将 FigureCanvas 添加到布局中
        layout.addWidget(self.canvas)

        # 获取屏幕的最大尺寸
        screen = QApplication.primaryScreen()
        geometry = screen.availableGeometry()
        max_width = geometry.width()
        max_height = geometry.height()

        print(f"Maximum Width: {max_width}")
        print(f"Maximum Height: {max_height}")

if __name__ == '__main__':
    app = QApplication(sys.argv)
    main_window = MainWindow()
    main_window.show()
    sys.exit(app.exec_())
