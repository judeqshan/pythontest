from functools import wraps

def hello_np(fn):
    def wrapper(*args,**kwargs):
        print("hello, %s" % fn.__name__)
        fn(*args, **kwargs)
        print("goodby, %s" % fn.__name__)
    return wrapper

def hello_p(country):
    def dec(fn):
        def wrapper(*args,**kwargs):
            print('hello, %s' % country)
            print("hello, %s" % fn.__name__)
            fn(*args, **kwargs)
            print("goodby, %s" % fn.__name__)
        return wrapper
    return dec

@hello_np  
# @hello_p("china")
def foo(fp1):
    print("i am foo")
    print(fp1)



def logged(func):
    @wraps(func)
    def with_logging(*args, **kwargs):
        print(func.__name__ + " was called")
        return func(*args, **kwargs)
    return with_logging

@logged
def f(x):
   """does some math"""
   return x + x * x

def main():
    # foo("1--")
    # print(test.test_req)
    # print(f.__name__)
    # print(f.__doc__)
    # f(2)
    foo("test")

if __name__ == '__main__':
    main()
