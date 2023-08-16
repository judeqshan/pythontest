addr = 0x02000000

print(hex((((addr) & 0xFE000000) >> 11) | ((addr) & 0x00007FFF)))

addr1 = 0X10
print(hex((addr1&0x10) >> 1))