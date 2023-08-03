arr = [1, 2, 3, 4, 5]
target = 4


def bsr(arr, target, left, right):
    if left > right:
        return -1
    mid = (left + right) // 2
    if arr[mid] == target:
        return mid
    elif arr[mid] < target:
        return bsr(arr, target, mid + 1, right)
    else:
        return bsr(arr, target, left, mid - 1)


print(bsr(arr, 4, 0, 4))
