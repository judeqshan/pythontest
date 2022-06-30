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

# https://stackoverflow.com/questions/308999/what-does-functools-wraps-do
# it will print with_logging because that's the name of your new function. 
# In fact, if you look at the docstring for f, 
# it will be blank because with_logging has no docstring, 
# and so the docstring you wrote won't be there anymore. 
# Also, if you look at the pydoc result for that function, 
# it won't be listed as taking one argument x; 
# instead it'll be listed as taking *args and **kwargs 
# because that's what with_logging takes.

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
    print(f.__name__)
    print(f.__doc__)


if __name__ == '__main__':
    main()
