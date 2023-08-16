import struct

def unpack_data(data, format_string):
    return struct.unpack(format_string, data)

     
# New code starts here
# Define a list of data to be unpacked
data_list = [b'\x01\x02\x03\xEf', b'\x05\x06\x07\x08', b'\x09\x0A\x0B\x0C']

# Define a format string for the data
format_string = '<BBBh'

# Unpack the data using the format string
for data in data_list:
    unpacked_data = unpack_data(data, format_string)
    print(unpacked_data)