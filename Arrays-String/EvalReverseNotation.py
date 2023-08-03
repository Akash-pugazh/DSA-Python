def EvalReverseNotation(tokens):
    if len(tokens) == 1:
        return int(tokens[0])
    stack = []
    for i in range(len(tokens)):
        stack.append(tokens[i])
        if tokens[i] in ["+", "-", "*", "/"]:
            operator = stack.pop()
            op2 = int(stack.pop())
            op1 = int(stack.pop())
            if operator == "+":
                stack.append(op1 + op2)
            elif operator == "-":
                stack.append(op1 - op2)
            elif operator == "*":
                stack.append(op1 * op2)
            else:
                stack.append(int(op1 / op2))
    return stack[0]


print(
    EvalReverseNotation(
        ["10", "6", "9", "3", "+", "-11", "*", "/", "*", "17", "+", "5", "+"]
    )
)
