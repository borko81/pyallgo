import numpy
import array
L = list(range(10))
L2 = [str(c) for c in L]
print(L2)
# hetoregenen list
L3 = [True, "2", 3.24, 5]
print([type(x) for x in L3])

L_ARR = array.array('i', L)
print(L_ARR)