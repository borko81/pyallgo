numbers = [1, 2, 3, 4, 5]
letter = 'some name'


def my_sum(numbers):
    if len(numbers) == 0:
        return 0
    head, tail = numbers[0], numbers[1:]
    return head + my_sum(tail)


def reverse_letter(letter):
    if len(letter) in (0, 1):
        return letter
    head, tail = letter[0], letter[1:]
    return reverse_letter(tail) + head


print(my_sum(numbers))
print(reverse_letter(letter))
