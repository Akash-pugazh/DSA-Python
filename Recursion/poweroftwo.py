# Leetcode Problem


class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        if n in [1, 2]:
            return True
        else:
            if n % 3 == 0 or n == 0:
                return False
            else:
                return self.isPowerOfTwo(int(n / 2))


test1 = Solution().isPowerOfTwo(16)
test2 = Solution().isPowerOfTwo(-132131)
test3 = Solution().isPowerOfTwo(1)

print(test1)
print(test2)
print(test3)
