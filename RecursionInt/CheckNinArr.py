arr = [1, 2, 3, 4, 5]


def checkNinArray(arr, n):
    if arr[0] == n:
        return True
    if len(arr) > 1:
        return checkNinArray(arr[1:], n)
    return False


print(checkNinArray(arr, 1))
