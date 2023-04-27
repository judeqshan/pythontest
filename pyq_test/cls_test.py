class A(object):
    a = 'a'
    @staticmethod
    def foo1(name):
        print('hello', name)
        print(A.a) # 正常
        print(A.foo2('mamq')) # 报错: unbound method foo2() must be called with A instance as first argument (got str instance instead)
    def foo2(self, name):
        print('hello', name)
    @classmethod
    def foo3(cls, name):
        print('hello', name)
        print(A.a)
        print(cls().foo2(name))

