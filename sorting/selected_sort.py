def selected_sort(arr, size):
    for x in range(size):
        min_idx = x

        for i in range(x + 1, size):
            if arr[min_idx] > arr[i]:
                min_idx = i

        arr[min_idx], arr[x] = arr[x], arr[min_idx]


if __name__ == '__main__':
    data = [7, 2, 1, 6]
    size = len(data)
    selected_sort(data, size)
    print(data)
