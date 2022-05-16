def count_down(start: int) -> None:
    print(start)
    start -= 1
    if start > 0:
        count_down(start)


def rec_sum(n):
    if n > 0:
        return n + rec_sum(n - 1)
    return 0


if __name__ == '__main__':
    print(rec_sum(10))
