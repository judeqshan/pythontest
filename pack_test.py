import struct

# native byteorder
buffer = struct.pack("I", 1)
print(repr(buffer))

