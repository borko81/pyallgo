numbers = [1, 2, 3, 4, 5]


def my_sum(numbers):
    if len(numbers) == 0:
        return 0
    head, tail = numbers[0], numbers[1:]
    return head + my_sum(tail)


print(my_sum(numbers))