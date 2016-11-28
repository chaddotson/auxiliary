
from ctypes import *



class test_t(Structure):
    _fields_ = [
        ("number", c_int)
    ]

    #nested_t *nested;


size = c_int(0);


with open("test.bin", "rb") as f:

    size = c_int.from_buffer_copy(f.read(4))
    buffer(size)[0] = 2
    print "size:", size
