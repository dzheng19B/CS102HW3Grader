def evalRPN(tokens: List[str]) -> int:

    stack = []
    for e in tokens:
        
        if e == "+":
            stack.append(stack.pop() + stack.pop())
        
        elif e == "-":
            second = stack.pop()
            first = stack.pop()
            stack.append(first - second)

        elif e == "*":
            
            stack.append(stack.pop() * stack.pop())
        
        elif e == "/":
            second = stack.pop()
            first = stack.pop()
            stack.append(int(first / second))
        
        else:
            stack.append(int(e))
        
    return stack[0]