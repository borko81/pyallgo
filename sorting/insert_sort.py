arr_elements = [2, 1, 10, 23]


def insert_sort(array):
    for x in range(1, len(array)):
        for y in range(x, 0, -1):
            if array[y] < array[y - 1]:
                array[y], array[y - 1] = array[y - 1], array[y]


insert_sort(arr_elements)
print(arr_elements)
