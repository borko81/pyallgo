def sum_recursive(current: int, sum: int, finish=100) -> int:
    if current == finish:
        return sum
    return sum_recursive(current + 1, sum + current, finish)


# with use global variable
current = 9
sum = 0


def sum_with_global():
    global current
    global sum
    if current == 11:
        return sum
    sum += current
    current += 1
    return sum_with_global()


if __name__ == '__main__':
    # # print(sum_recursive(9, 0, 11))
    print(sum_with_global())
