class parent(object):
    def __init__(self) -> None:
        pass
    def test(self):
        print("parent test")
        

class son(parent):
    def __init__(self) -> None:
        super().__init__()
    def test(self):
        print("son test")
        

if __name__ == "__main__":
    s = son()
    s.test()