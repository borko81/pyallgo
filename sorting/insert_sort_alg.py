l = [int(x) for x in input().split(" ")]


def insert_sorted(array):
    for idx in range(len(array)):
        min_idx = idx
        for next_ind in range(idx + 1, len(array)):
            if array[next_ind] < array[min_idx]:
                min_idx = next_ind
        array[idx], array[min_idx] = array[min_idx], array[idx]
    print(array)


insert_sorted(l)
