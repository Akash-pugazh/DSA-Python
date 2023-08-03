def calPoints(operations):
    stack = []
    for operation in operations:
        if operation == "+":
            stack.append(stack[-2] + stack[-1])
        elif operation == "D":
            stack.append(stack[-1] * 2)
        elif operation == "C":
            stack.pop()
        else:
            stack.append(int(operation))
        print(stack)
    return sum(stack)
