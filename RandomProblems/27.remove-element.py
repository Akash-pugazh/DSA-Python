#
# @lc app=leetcode id=27 lang=python3
#
# [27] Remove Element
#


# @lc code=start
class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        startPtr = 0
        endPtr = len(nums) - 1
        while startPtr <= endPtr:
            if  nums[startPtr] == val:
                nums[startPtr], nums[endPtr] = nums[endPtr], "_"
                endPtr -= 1
            else:
                startPtr += 1 
        return endPtr + 1


# @lc code=end
