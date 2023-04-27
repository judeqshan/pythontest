# -*- coding: utf-8 -*-
import sys

from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *


class TimeThread(QThread):
    signal_time = pyqtSignal(str, int)  # 信号

    def __init__(self, parent=None):
        super(TimeThread, self).__init__(parent)
        self.working = True
        self.num = 0

    def start_timer(self):
        self.num = 0
        self.start()

    def run(self):
        while self.working:
            print("Working", self.thread())
            self.signal_time.emit("Running time:", self.num)  # 发送信号
            self.num += 1
            self.sleep(1)


class TimeDialog(QWidget):
    def __init__(self):
        super(TimeDialog, self).__init__()
        self.timer_tv = QTextBrowser(self)
        self.init_ui()
        self.timer_t = TimeThread()
        self.timer_t.signal_time.connect(self.update_timer_tv)

    def init_ui(self):
        self.resize(300, 200)
        self.setWindowTitle('TimeDialog')
        self.timer_tv.setText("Wait")
        self.timer_tv.setGeometry(QRect(10, 145, 198, 26))
        self.timer_tv.move(0, 15)

        btn1 = QPushButton('Quit', self)
        btn1.setToolTip('Click to quit')
        btn1.resize(btn1.sizeHint())
        btn1.move(200, 150)
        btn1.clicked.connect(QCoreApplication.instance().quit)

        start_btn = QPushButton('Start', self)
        start_btn.setToolTip("Click to start")
        start_btn.move(50, 150)
        # self.connect(start_btn, SIGNAL("clicked()"), self.click_start_btn)
        start_btn.clicked.connect(self.click_start_btn)

    def click_start_btn(self):
        self.timer_t.start_timer()

    def update_timer_tv(self, text, number):
        self.timer_tv.setText(self.tr(text + " " + str(number)))


if __name__ == '__main__':
    app = QApplication(sys.argv)
    time_dialog = TimeDialog()
    time_dialog.show()

    sys.exit(app.exec_())