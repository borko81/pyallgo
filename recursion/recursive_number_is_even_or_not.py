def what_is_number(n):
    if n < 2:
        return n % 2 == 0
    return what_is_number(n - 2)


print(what_is_number(3))