t = (1, 2)
another_t = (3,)
t = t.__add__(another_t)
print(t)
print(t.__contains__(3))
print(t.__getitem__(2))
print(t.__len__())
a, b, *_ = t
print(divmod(b, a))

print(eval("+".join(str(x) for x in range(1, 101))))
print([*range(4), 8, *range(10, 16)])