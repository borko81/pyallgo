from functools import lru_cache


@lru_cache(maxsize=None)
def factory(x: int) -> int:
    """
    Return factory recursion function
    :param x: int
    :return: int
    """
    if x == 1:
        return 1
    return x * factory(x - 1)


if __name__ == '__main__':
    search_num = 100
    result = factory(search_num)
    print(f"The factory of result {search_num} is {result}")