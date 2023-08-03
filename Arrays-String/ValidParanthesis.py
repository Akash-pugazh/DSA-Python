def ValidParanthesis(s: str) -> bool:
    # Base condition
    if s[0] in [")", "]", "}"]:
        return False
    stack = []
    top = len(stack) - 1

    for char in s:
        stack.append(char)
        if stack[0] in [")", "]", "}"]:
            return False
        if (
            stack[top] == ")"
            and stack[top - 1] == "("
            or stack[top] == "]"
            and stack[top - 1] == "["
            or stack[top] == "}"
            and stack[top - 1] == "{"
        ):
            stack.pop()
            stack.pop()
    if len(stack) == 0:
        return True
    return False


print(ValidParanthesis("(){}}{"))
