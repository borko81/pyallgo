import random

array = [random.randint(1, 100) for _ in range(20)]
print(array)


def merge_sort(nums):
    if len(nums) > 1:

        mid = len(nums) // 2

        L = nums[:mid]
        R = nums[mid:]

        merge_sort(L)
        merge_sort(R)

        i = j = k = 0

        while i < len(L) and j < len(R):
            if L[i] < R[j]:
                nums[k] = L[i]
                i += 1
            else:
                nums[k] = R[j]
                j += 1
            k += 1

        while i < len(L):
            nums[k] = L[i]
            i += 1
            k += 1

        while j < len(R):
            nums[k] = R[j]
            j += 1
            k += 1


merge_sort(array)
print(array)
