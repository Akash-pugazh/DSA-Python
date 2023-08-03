# LeetCode Problem
class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        if n in [1]:
            return True
        else:
            if not n % 3 == 0 or n == 0:
                return False
            else:
                return self.isPowerOfThree(int(n / 3))


test1 = Solution().isPowerOfThree(27)
test2 = Solution().isPowerOfThree(0)
test3 = Solution().isPowerOfThree(-1)

print(test1)
print(test2)
print(test3)
