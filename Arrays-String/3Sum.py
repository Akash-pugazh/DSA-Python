from typing import List


def ThreeSum(nums: List[int]) -> List[List[int]]:
    res: List[int] = []
    nums.sort()

    for index, value in enumerate(nums):
        if index > 0 and nums[index - 1] == value:
            continue

        leftPtr: int = index + 1
        rightPtr: int = len(nums) - 1

        while leftPtr < rightPtr:
            threeSumValue: int = value + nums[leftPtr] + nums[rightPtr]
            if threeSumValue < 0:
                leftPtr += 1
            elif threeSumValue > 0:
                rightPtr -= 1
            else:
                res.append([value, nums[leftPtr], nums[rightPtr]])
                leftPtr += 1
                while nums[leftPtr - 1] == nums[leftPtr] and leftPtr < rightPtr:
                    leftPtr += 1
    return res

print(ThreeSum([-1,0,1,2,-1,-4]))