n = 3
arr = [None] * n


def solve(ind, arr):
    if ind >= len(arr):
        print(*arr)
        return
    for i in range(1, len(arr) + 1):
        arr[ind] = i
        solve(ind + 1, arr)



if __name__ == '__main__':
    solve(0, arr)