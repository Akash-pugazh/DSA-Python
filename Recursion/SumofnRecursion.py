def sumofnRecursion(n):
    assert n >= 0, "Number should be positive"
    if n == 0:
        return 0
    else:
        return int(n % 10) + sumofnRecursion(int(n / 10))


print(sumofnRecursion(11))
