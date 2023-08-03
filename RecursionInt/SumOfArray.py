arr = [1, 2, 3, 4, 5]


def sumOfArr(arr):
    if len(arr) == 1:
        return arr[0]
    return arr[0] + sumOfArr(arr[1:])


print(sumOfArr(arr))
