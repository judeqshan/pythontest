import ctypes
class t_resp(ctypes.Structure):
  _fields_ = [
    ('len', ctypes.c_int),
    ('data', ctypes.c_ubyte*4096 ),
  ]

c_resp = t_resp()
c_resp._fields_[1][1] = 1
resp = c_resp.data[0:c_resp.len]
# print("data = %x   %d" %(resp[0],resp[0]))
ret=resp[1]+(resp[2]<<8)+(resp[3]<<16)+(resp[4]<<24)



