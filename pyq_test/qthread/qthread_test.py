from PyQt5.Qt import (QApplication, QWidget, QPushButton,
                      QThread)
from PyQt5.QtCore import QThread, QWaitCondition, QMutex, pyqtSignal
import sys
import time

Q_MUT_1 = QMutex()
Q_MUT_2 = QMutex()

# 继承QThread
class Thread_1(QThread):  # 线程1
    def __init__(self):
        super().__init__()
        
    def run(self):
        Q_MUT_1.lock()
        print('Thread_1 id', QThread.currentThread())
        values = [1, 2, 3, 4, 5]
        for i in values:
            print(i)
            time.sleep(1)  # 休眠
        Q_MUT_1.unlock()
            
class Thread_2(QThread):  # 线程2
    def __init__(self):
        super().__init__()
        
    def run(self):
        Q_MUT_2.lock()
        print('Thread_2 id', QThread.currentThread())
        values = ["a", "b", "c", "d", "e"]
        for i in values:
            print(i)
            time.sleep(1)
        Q_MUT_2.unlock()
        
        
class MyWin(QWidget):
    def __init__(self) -> None:
        super().__init__()
        self.btn_1 = QPushButton('按钮1',self)
        self.btn_1.move(120,80)
        self.btn_1.clicked.connect(self.click_1)
        self.btn_1.setObjectName("btn_1")
        
        self.btn_2 = QPushButton('按钮2',self)
        self.btn_2.move(120,120)
        self.btn_2.clicked.connect(self.click_2)
        self.btn_2.setObjectName("btn_2")
    
    def click_1(self):
        # values = [1,2,3,4,5]
        # for i in values:
        #     print(i)
        #     time.sleep(5)
        self.thread_1 = Thread_1()
        self.thread_1.start()
                    
    def click_2(self):
        # values = ["a","b","c","d","e"]
        # for i in values:
        #     print(i)
        #     time.sleep(5)
        self.thread_2 = Thread_2()
        self.thread_2.start()
            

if __name__ == "__main__":
    app = QApplication(sys.argv)
    myshow = MyWin()
    myshow.show()
    sys.exit(app.exec_())            
    
    