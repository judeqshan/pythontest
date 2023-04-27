def adder(a=0, b=0, ci=0, sub=0):
    return a-b+ci if sub == 1 else a+b+ci
def b8_21selector(a=0, b=0, sel=0):
    return a if sel == 0 else b
def register():
    temp = 0
    def register_inner(data=0, w=0):
        nonlocal temp
        if w == 1:
            temp = data
        return temp
    return register_inner
def int2bin(data=0, length=8, tuple_=1, string=0, humanOrder=0):
    #辅助函数，整数转换为二进制字符串或者元祖。
    r = bin(data)[2:].zfill(length)
    r = r[::-1] if humanOrder == 0 else r
    return r if string == 1 else tuple(int(c) for c in r)
def cpu():
    pc = 0 # pc 计数器从 0 开始，无限循环。
    IR, DR, AC = register(), register(), register() # 新建寄存器
    ramc = [0x18, 0x19, 0x1d, 0x02, 0x31, 0x30, 0x00] # 初始化代码
    ramd = [10, 2, 3, 0xff, 0x06, 0x02] # 初始化数据

    IR(0, w=1) # 初始化寄存器
    DR(0, w=1)
    AC(0, w=1)
    while True:
        IR(ramc[pc], w=1) # 指令读写
        *_, pre, dr, ac, sub, w, s21 = int2bin(IR(), humanOrder=1) # 指令解码
        if IR() == 0:
            break # HLT信号
        DR(ramd[pc], w=dr) # 数据读写
        r = adder(AC(), DR(), sub=sub) # 加法器自动加法
        AC(b8_21selector(DR(), r, s21), w=ac) # 选择器选择后，累加寄存器读写
        ramd[pc] = AC() if w else ramd[pc] # 根据 w 信号，数据写入 RAM
        zf = (AC() == 0) # 零标志位寄存器
        pc = DR() if (pre == 1 and zf == True and s21 == 1) else pc + 1 # Jz 指令跳转
        pc = DR() if (pre == 1 and s21 == 0) else pc # 无条件跳转 Jmp
        print(AC()) 
if __name__ == '__main__':
    cpu()