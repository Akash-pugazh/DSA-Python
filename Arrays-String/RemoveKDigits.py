def removeKDigits(num: str, k: int):
    stack = []
    for n in num:
        while k and stack and stack[-1] > n:
            k -= 1
            stack.pop()
        if stack or n != "0":
            stack.append(n)

    stack = stack[: len(stack) - k]
    res = "".join(stack)
    return res if res else "0"


print(removeKDigits("1432219", 3))
