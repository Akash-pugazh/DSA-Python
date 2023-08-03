import math

piles = [3, 6, 7, 11]
h = 8


def KokoBananas(piles, h):
    l, r = 1, max(piles)
    res = r
    while l <= r:
        m = (l + r) // 2
        hrs = 0
        for p in piles:
            hrs += math.ceil(p / m)
        if hrs > h:
            l = m + 1
        else:
            res = m
            r = m - 1
    return res


print(KokoBananas(piles, h))
