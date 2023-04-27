import ctypes

class TestInt:
  def __init__( self,slib=f"/home/virtualpc/Alphawave/test/build/linux/c_test.so"):
    self.clib = ctypes.CDLL(slib)
  
  def hello(self):
    num = self.clib.cHi()
    print("output = 0x%x"%(num))


if __name__ == '__main__':
    ti = TestInt()
    ti.hello()
