def GcdRecursion(a, b):

    assert int(a) == a and int(b) == b, "Parameters must be integer"

    if a < 0:
        a = -1 * a
    if b < 0:
        b = -1 * b

    if b == 0:
        return a
    else:
        return GcdRecursion(b, a % b)


print(GcdRecursion(-8, 12))