def threeSumClosest(nums, target):
    temp = []
    nums.sort()
    for index, value in enumerate(nums):
        if index > 0 and nums[index - 1] == value:
            continue
        l, r = index + 1, len(nums) - 1
        while l < r:
            threeSum = value + nums[l] + nums[r]
            temp.append(threeSum)
            if threeSum < target:
                l += 1
            elif threeSum > target:
                r -= 1
            else:
                return threeSum
    temp.append(target)
    temp.sort()
    for index, value in enumerate(temp):
        if value == target:
            if index == 0:
                return temp[index + 1]
            elif index == len(temp) - 1:
                return temp[index - 1]
            else:
                prevTargetDiff = abs(target - temp[index - 1])
                nextTargetDiff = abs(target - temp[index + 1])
                return (
                    temp[index - 1]
                    if prevTargetDiff < nextTargetDiff
                    else temp[index + 1]
                )


print(threeSumClosest([-1, 2, 1, -4], 1))
