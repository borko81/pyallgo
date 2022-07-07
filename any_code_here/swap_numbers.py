import random

l_numbers = [random.randint(1, 100) for _ in range(10)]
print(l_numbers)


def swap_it(l):
    for pos, num in enumerate(l):
        if pos >= len(l) // 2:
            l[pos], l[len(l) - 1 - pos] = l[len(l) - 1 - pos], l[pos]



if __name__ == '__main__':
    swap_it(l_numbers)
    print(l_numbers)
