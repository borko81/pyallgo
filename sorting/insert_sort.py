arr_elements = [2, 1, 10, 23]


def insert_sort(array):
    for x in range(1, len(array)):
        for y in range(x, 0, -1):
            if array[y] < array[y - 1]:
                array[y], array[y - 1] = array[y - 1], array[y]
            else:
                break


def insert_sort_two(array):
    for x in range(len(array)):
        j = x
        while j > 0 and array[j] < array[j - 1]:
            array[j], array[j - 1] = array[j - 1], array[j]
            j -= 1


insert_sort_two(arr_elements)
print(arr_elements)
