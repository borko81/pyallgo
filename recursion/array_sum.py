from time import perf_counter
from threading import Thread


numbers = [int(x) for x in range(1, 11)]
result = []


def calc_sum(nums, idx):
    if idx == len(nums) - 1:
        return nums[idx]
    return nums[idx] + calc_sum(nums, idx + 1)


def calc_sum_two(nums, counter=0):
    counter += nums.pop()
    if len(nums) == 0:
        return counter
    return counter + calc_sum_two(nums)


if __name__ == '__main__':
    start_time = perf_counter()
    print(calc_sum(numbers, 0))
    print(calc_sum_two(numbers))
    print("---%.3f seconds---" % (perf_counter() - start_time))
