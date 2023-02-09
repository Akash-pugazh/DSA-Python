
class Solution:
    def DecimalToBinary(self, n, result = ""):
        assert 0 <= n == int(n), "N value should be a postive integer"
        if n == 1:
            return f"1{result}"
        elif n == 0:
            return 0
        else:
            result += str(n % 2)
            return self.DecimalToBinary(int(n / 2), result)


test1 = print(Solution().DecimalToBinary(16))
test2 = print(Solution().DecimalToBinary(8))
test3 = print(Solution().DecimalToBinary(1.3))
