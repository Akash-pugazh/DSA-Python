def powerofnRecursion(n, power):
    assert 0 <= power == int(power), "Power value should be a non-negative number"
    if power == 0:
        return 1
    elif power == 1:
        return  n
    else:
        return n * powerofnRecursion(n, power - 1)


print(powerofnRecursion(2, -2))
