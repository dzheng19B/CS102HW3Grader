def evalRPN(tokens: List[str]) -> int:
    stack = []
    for i in tokens:
        if i == "+":
            x1 = stack.pop()
            x2 = stack.pop()
            y = x1 + x2
            stack.append(y)
        elif i == "-":
            x1 = stack.pop()
            x2 = stack.pop()
            y = x2 - x1
            stack.append(y)
        elif i == "/":
            x1 = stack.pop()
            x2 = stack.pop()
            y = x2 / x1
            stack.append(y)
        elif i == "*":
            x1 = stack.pop()
            x2 = stack.pop()
            y = x1 * x2
            stack.append(y)
        else:
            stack.append(i)
    return stack.pop()