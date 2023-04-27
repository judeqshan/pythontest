import time


class delay():
    def __init__(self,duration) -> None:
    # def __init__(self) -> None:
        pass
        self.duration = duration
        print("in delay __init__")
    
    # def __call__(self, *args, **kwdsy):
    def __call__(self, func):
        pass
        def wrapper(*args, **kwdsy):
            print("before time sleep\n")
            func(*args, **kwdsy)
            time.sleep(self.duration)
            print("after time sleep\n")
        return wrapper
   
# d = delay()     
# d(3)

@delay(duration=3)
def add(a, b):
    print (a+b)
    
    
add(2,3)

def sub(a,b):
    print(a-b)

class DelayFunc:
    def __init__(self):
        # self.duration = duration
        # self.func = func
        pass

    def __call__(self, *args, **kwargs):
        print(args)
        print(kwargs)
        # print(f'Wait for {self.duration} seconds...')
        # time.sleep(self.duration)
        # return self.func(*args, **kwargs)
        return args[0]
    


import functools

def delay():
  
    return DelayFunc



@DelayFunc()
def add(a, b):
     print(a+b)

add(3,5)