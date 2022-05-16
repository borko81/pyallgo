def bubble_sort(elements: list) -> None:
    n: int = len(elements)
    for x in range(n):
        for y in range(0, n - x - 1):
            if elements[y] > elements[y + 1]:
                elements[y], elements[y + 1] = elements[y + 1], elements[y]


if __name__ == '__main__':
    arr_elements = [2, 1, 10, 23]
    bubble_sort(arr_elements)
    print(", ".join([str(x) for x in arr_elements]))
