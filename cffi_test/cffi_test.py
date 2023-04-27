from cffi import FFI
ffi = FFI()
ffi.cdef("""
    int add(int a, int b);
    int sub(int a, int b);
""")
#verify是在线api模式的基本方法它里面直接写C代码即可
lib = ffi.verify("""
    int add(int a,int b){
        return a+b;
    }
     int sub(int a,int b){
        return a-b;
    }

""")
print(lib.add(10,2))
print(lib.sub(10,2))