arr = [1291, 897, 4566, 1232, 80, 700]
size = len(arr)


def shell_sorting(array, n):
    interval = n // 2
    while interval > 0:
        for i in range(interval, n):
            temp = array[i]
            j = i
            while j >= interval and array[j - interval] > temp:
                array[j] = array[j - interval]
                j -= interval

            array[j] = temp
        interval //= 2


shell_sorting(arr, size)
print(arr)