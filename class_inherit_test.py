class A(object):
    def __init__(self) -> None:
        self.a="a"
        
    def funA(self):
        print("in A.funA")

class B(object):
    def __init__(self) -> None:
        self.b="b"
        
    def funB(self):
        print("in B.funB")

class C(A, B):
    def testA(self):
        print(self.a)
    def funC(self):
        print("in C.funC")


if __name__ == "__main__":
    c_test = C()
    c_test.testA()
