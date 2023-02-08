def fibonacciRecursion(n):
    assert 0 <= n == int(n), "Number should be positive and a integer"

    if n in [0, 1]:
        return n
    else:
        return fibonacciRecursion(n - 1) + fibonacciRecursion(n - 2)


print(fibonacciRecursion(5))
