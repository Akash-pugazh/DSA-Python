def Factorial(n):
    assert n >= 1, "Your N value should be positive to find factorial"
    if n in [0, 1]:
        return 1
    else:
        return n * Factorial(n - 1)


print(Factorial(-4))