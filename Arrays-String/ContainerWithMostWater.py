height = [2, 3, 4, 5, 18, 17, 6]


def container_with_most_water(height: list):
    maximumArea = float("-inf")
    startPtr = 0
    endPtr = len(height) - 1

    while startPtr < endPtr:
        minPtr = min(height[startPtr], height[endPtr])
        area = minPtr * (endPtr - startPtr)
        maximumArea = max(maximumArea, area)
        print(startPtr, endPtr)
        if height[startPtr] < height[endPtr]:
            startPtr += 1
        else:
            endPtr -= 1
    return maximumArea


print(container_with_most_water(height))
