import random

array = [random.randint(1, 100) for _ in range(20)]
print(array)


def quick_sort(array):
    if len(array) <= 1:
        return array
    pivot = array.pop()

    minimum_values = []
    maximum_values = []

    for item in array:
        if item < pivot:
            minimum_values.append(item)
        else:
            maximum_values.append(item)

    return quick_sort(minimum_values) + [pivot] + quick_sort(maximum_values)


array = quick_sort(array)
print(array)
