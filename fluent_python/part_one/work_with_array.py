from array import array
from random import random

floats_numbers = array('d', (random() for _ in range(10 * 7)))

# fp = open('floats.bin', 'wb')
# floats_numbers.tofile(fp)
# fp.close()

file = open('floats.bin', 'rb')
new_floats_numbers = array('d')
new_floats_numbers.fromfile(file, 10 * 7)
file.close()
print(len(new_floats_numbers))

int_array = array('i', [1, 2, 3, 4, 5])
int_array.append(6)

try:
    int_array.remove(11)
except ValueError as e:
    print(e)

int_array.insert(1, -20)
int_array[0] = 11
print(int_array.tolist())
