nums = [4, 5, 6, 7, 0, 1, 2]

target = 3


def searchRotated(nums, target):
    l, r = 0, len(nums) - 1
    while l <= r:
        m = (l + r) // 2
        if nums[m] == target:
            return m
        if nums[l] <= nums[m]:
            if target >= nums[l] and target <= nums[m]:
                r = m - 1
            else:
                l = m + 1
        else:
            if target >= nums[m] and target <= nums[r]:
                l = m + 1
            else:
                r = m - 1
    return -1


print(searchRotated(nums, target))
