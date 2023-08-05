#
# @lc app=leetcode id=2161 lang=python3
#
# [2161] Partition Array According to Given Pivot
#
from typing import List, Set, Dict, Tuple, Union, Any
# @lc code=start
class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        l, s, g = [], [], []
        for num in nums:
            if num < pivot:
                l.append(num)
            elif num == pivot:
                s.append(num)
            else:
                g.append(num)
        return l + s + g
        
# @lc code=end

