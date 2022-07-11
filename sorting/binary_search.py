# work only in sorted list

user_array = [int(x) for x in '1 2 3 4 5'.split()]
user_target = 2


def binary_search(array, targer):
    left = 0
    right = len(array) - 1
    while left <= right:
        mid_idx = (left + right) // 2
        mid_el = array[mid_idx]

        if mid_el == targer:
            return mid_idx

        if mid_el < targer:
            left = mid_idx + 1
        else:
            right = mid_idx - 1
    return -1


print(binary_search(user_array, user_target))
