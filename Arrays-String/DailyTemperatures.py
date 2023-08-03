def dailyTemperatures(temperatures):
    stack = []
    res = [0] * len(temperatures)
    for index, temperature in enumerate(temperatures):
        while stack and temperature > stack[-1][0]:
            stackTemperature, stackIndex = stack.pop()
            res[stackIndex] = index - stackIndex
        stack.append((temperature, index))
    return res
