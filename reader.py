
from ctypes import *

class nest_t(Structure):
    _fields_ = [
        ("a", c_int),
        ("b", c_int),
        ("c", c_float),
    ]


class test_t(Structure):
    _fields_ = [
        ("number", c_int),
        ("nested", POINTER(nest_t))
    ]

    #nested_t *nested;


size = c_int(0);

test = None



with open("test.bin", "rb") as f:

    size = c_int.from_buffer_copy(f.read(4))
    
    test = (test_t * size.value)()


    #buffer(size)[0] = 2
    print("size:", size)

    for i in range(0, size.value):
        number_of_nested = c_int.from_buffer_copy(f.read(4))
        test[i].number = number_of_nested

        print("Number of nested:", number_of_nested)

        #test.nested = pointer(POINTER(nest_t * number_of_nested.value))

        arr_t = (nest_t * number_of_nested.value)
        test[i].nested = cast(arr_t(), POINTER(nest_t))


        for j in range(0, number_of_nested.value):
            #temp = nest_t.from_buffer_copy(f.read(sizeof(nest_t)))
            test[i].nested[j] = nest_t.from_buffer_copy(f.read(sizeof(nest_t)))
            print( test[i].nested[j].a,  test[i].nested[j].b,  test[i].nested[j].c)
            
            #test.nested[j].contents = temp



print("Read:", size.value)

for i in range(0, size.value):            
    count = test[i].number
    for j in range(0, count):
        print(i, j, test[i].nested[j].a, test[i].nested[j].b, test[i].nested[j].c)


