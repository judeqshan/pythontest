import atexit

def atexitFunc_1():
    print("这是测试一号")

def atexitFunc_2(name, age):
    print('这是测试二号, %s is %d' % (name, age))

atexit.register(atexitFunc_1)
atexit.register(atexitFunc_2, 'tom', 20)

@atexit.register
def atexitFunc_3():
    print('这是测试三号')
