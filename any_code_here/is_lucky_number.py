arr = [1291, 897, 4566, 1232, 80, 700]


def is_lucky_or_not(n):
    ar = [0] * 10

    while n > 0:
        digit = n % 10
        if ar[digit]:
            return False

        n //= 10
        n = int(n)
        ar[digit] = 1

    return True


if __name__ == '__main__':
    for n in arr:
        check = is_lucky_or_not(n)
        if check:
            print("{} is lucky number".format(n))
        else:
            print("{} is not lucky number".format(n))
