# Leet Code Problem
class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        if n == 1:
            return True
        else:
            if not n % 4 == 0 or n == 0:
                return  False
            else:
                return self.isPowerOfFour(int(n / 4))

test1 = print(Solution().isPowerOfFour(16))
test1 = print(Solution().isPowerOfFour(5))
test1 = print(Solution().isPowerOfFour(1))
