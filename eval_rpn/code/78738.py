def evalRPN(tokens: List[str]):
    stack = []
    operator = ["+","-","*","/"]
    for i in tokens:
        if i not in operator:
            stack.append(i)
        else:
            val1 = int(stack.pop()) 
            val2 = int(stack.pop())
            if i == "/":
                result = val2//val1

            else:
                if i == "+":
                    result = val2+val1
                elif i == "-":
                    result = val2-val1
                elif i == "*":
                    result = val2*val1
            stack.append(result)
    return stack[0]