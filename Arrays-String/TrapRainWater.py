from typing import List

height = [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]


# rightMaxArr: List[int] = [0] * (len(height))
# rightPtr: int = len(rightMaxArr) - 2
# maxValue: int = height[-1]

# while rightPtr >= 0:
#     rightMaxArr[rightPtr] = maxValue
#     if height[rightPtr] > maxValue:
#         maxValue = height[rightPtr]
#     rightPtr -= 1
# print(rightMaxArr)


def trapRainWater(height: List[int]) -> int:
    ptr: int = 0
    result: int = 0
    leftMax: int = 0
    rightMax: int = 0
    while ptr < len(height):
        value: int = height[ptr]
        if value > leftMax:
            leftMax = value

        rightMax: int = max(height[ptr + 1 :]) if ptr != len(height) - 1 else 0

        minValue: int = min(leftMax, rightMax)
        if minValue != 0 and value < minValue:
            result += minValue - value

        ptr += 1
    return result


# print(trapRainWater(height))
