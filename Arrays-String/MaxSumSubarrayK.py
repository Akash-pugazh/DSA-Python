arr = [100, 200, 300, 400]
k = 2


def MaximumSubarraySumOfSizeK(arr: list, k: int):
    currentSum = sum(arr[:k])
    maxSum = currentSum

    for i in range(1, len(arr) - k + 1):
        currentSum = currentSum + arr[i + 1] - arr[i - 1]
        maxSum = max(currentSum, maxSum)

    return maxSum


print(MaximumSubarraySumOfSizeK(arr, k))
