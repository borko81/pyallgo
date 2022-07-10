def factorial(n):
    mapper = {}
    if n == 1:
        return 1
    mapper[n] = factorial(n - 1)
    return n + mapper[n]


print(factorial(50))


def convert_iteration_to_recursion(i=5):
    print("Number change to value %d" % i)
    i -= 1
    if i > 0:
        convert_iteration_to_recursion(i)
    else:
        return
    print(i)




convert_iteration_to_recursion()