def bubble_sort(elements: list) -> None:
    n: int = len(elements)
    for x in range(n):
        for y in range(0, n - x - 1):
            if elements[y] > elements[y + 1]:
                elements[y], elements[y + 1] = elements[y + 1], elements[y]


def bubble_sort_two(elements: list):
    counter = 0
    is_sorted = False
    while not is_sorted:
        is_sorted = True
        for x in range(1, len(elements) - counter):
            if elements[x] < elements[x - 1]:
                elements[x], elements[x - 1] = elements[x - 1], elements[x]
                is_sorted = False
        counter += 1


if __name__ == '__main__':
    arr_elements = [2, 1, 10, 23]
    bubble_sort_two(arr_elements)
    print(", ".join([str(x) for x in arr_elements]))
