n = 5


def write_recursive_figure(number):
    if number == 0:
        return
    print('*' * number)
    write_recursive_figure(number - 1)
    print('#' * number)


if __name__ == '__main__':
    write_recursive_figure(n)