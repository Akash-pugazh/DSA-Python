nums = [2, 5]
target = 5


def binarySearch(nums, target):
    result = -1
    l, r = 0, len(nums) - 1
    while l <= r:
        m = (l + r) // 2
        if nums[m] == target:
            result = m
            return result
        elif nums[m] < target:
            l = m + 1
        else:
            r = m - 1
    return result


print(binarySearch(nums, target))
