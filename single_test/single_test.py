# import threading
# class evb(object):
#     _instance_lock = threading.Lock()

#     def __init__(self,*args, **kwargs):
#         print("iniiiiiiitttttttttttttttttttt")
#         pass


#     def __new__(cls, *args, **kwargs):
#         print("neWWWWWWWWWWWWWWWWWWWWWWWWWWWW")
#         if not hasattr(evb, "_instance"):
#             with evb._instance_lock:
#                 if not hasattr(evb, "_instance"):
#                     evb._instance = object.__new__(cls)  
#         return evb._instance

#     def test(self):
#         print("testtttttttttttttttttttttttttttttt")

# class person(object):
#     def test(self):
#         print("test")

# single1 = evb("test")
# single2 = evb("gggggggggggg")

# single1.test()

# print(type(single1))




# print(id(single1) == id(single2))


class Singleton(object):
    def __init__(self, cls):
        self._cls = cls
        self._instance = {}
    def __call__(self):
        if self._cls not in self._instance:
            self._instance[self._cls] = self._cls()
        return self._instance[self._cls]

@Singleton
class Cls2(object):
    def __init__(self):
        pass
    
    def test(self):
        print("testtttttttttttttt")
    
cls1 = Cls2()
cls2 = Cls2()
print(id(cls1) == id(cls2))
cls1.test()