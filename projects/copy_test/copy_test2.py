from PyQt5.QtCore import QThread

from threading import Thread

class TestClass():
    def __init__(self, a) -> None:
        pass
        self.a = a
        print(f"self.id_a = {id(self.a)} id_a = {id(a)}")
    
    def show_selfida(self):
        print(f"self.id_a = {id(self.a)} self.a = {self.a}")


class QTTestClass(QThread):
    def __init__(self, a) -> None:
        super(QTTestClass, self).__init__()
        pass
        self.a = a
        print(f"self.id_a = {id(self.a)} id_a = {id(a)}")
    
    def show_selfida(self):
        print(f"self.id_a = {id(self.a)} self.a = {self.a}")

    def run(self):
        self.show_selfida()


class ThreadTestClass(Thread):
    def __init__(self, a) -> None:
        pass
        super(ThreadTestClass, self).__init__()
        print("init thread  -------------: {threading.currrent_thread()}")
        self.a = a
        # print(f"self.id_a = {id(self.a)} id_a = {id(a)}")
    
    def show_selfida(self):
        # but if enable below 2 lines, not ok. as two thread refer to the same id. and self.a change when enter into the second thread.
        print(f"self.id_a = {id(self.a)} self.a = {self.a}")
        print(f"self.a = {self.a} self.a = {self.a["num"]}")
        # print(f"self.id_a = {id(self.a)} self.a = {self.a} self.a = {self.a["num"]}") # only enable this, ok

    def run(self):
        self.show_selfida()


if __name__ == "__main__":
    thread_list={}
    a = {}

    # for num in range(1,3):
    #     a = {"num":num}
    #     # tc2 = TestClass(a)
    #     thread_list[num] = QTTestClass(a)
    #     thread_list[num].start()
    
    for num in range(1,3):
        a["num"] = num
        # tc2 = TestClass(a)
        thread_list[num] = ThreadTestClass(a)
        thread_list[num].start()
    
    
    