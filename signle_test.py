# -*- coding: utf-8 -*-
class Singleton(object):
    def __new__(cls, *args, **kwargs):
        if not hasattr(cls, '_instance'):
            print('before new')
            print(cls)
            cls._instance = object.__new__(cls, *args, **kwargs)
            print('after new')
            cls._instance.__Singleton_Init__(*args, **kwargs)
        return cls._instance
    def __init__(self):
        print("__init__")
        
    def __Singleton_Init__(self):
        print("__Singleton_Init__")
        
class BB(Singleton):
    pass
        
class CC(Singleton):
    pass
c = CC()
c1 = CC()
b=BB()
b1=BB()
b.a=2
b1.a=5
c.a=3
c1.a=4
print(id(c), id(c1))
print(b.a,b1.a, c.a, c1.a)

# class Singleton(object):
#     def __new__(cls, *args, **kwargs):
#         if not hasattr(cls, '_instance'):
#             print('in new')
#             cls._instance = object.__new__(cls, *args, **kwargs)
#             cls._instance.__Singleton_Init__(*args, **kwargs)
#         return cls._instance
        
    # def __Singleton_Init__(self):
    #     print("__Singleton_Init__")

# class Singleton(object):
#     __instance=None
#     def __init__(self):
#         pass
#     def __new__(cls,*args,**kwd):
#         if Singleton.__instance is None:
#             Singleton.__instance=object.__new__(cls,*args,**kwd)
#         return Singleton.__instance
        
# a = Singleton()
# b = Singleton()
# print(id(a),id(b))
