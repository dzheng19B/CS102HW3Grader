from typing import List

def evalRPN(tokens: List[str]) -> int:
    sum = 0
    stack = []
 
    for i in range(len(tokens)):
        if tokens[i] == "+" or tokens[i] == "-" or tokens[i] == "*" or tokens[i] == "/":
            num2 = stack.pop()
            num1 = stack.pop()
            if tokens[i] == "+":
                sum = num1 + num2
            elif tokens[i] == "-":
                sum = num1 - num2
            elif tokens[i] == "*":
                sum = num1 * num2
            else:
                sum = int(num1 / num2)
            stack.append(sum)
        else:
            stack.append(int(tokens[i]))

    return stack.pop()



print(evalRPN(["2", "1", "+", "3", "*"]))
print(evalRPN(["4", "13", "5", "/", "+"]))
print(evalRPN(["10", "6", "9", "3", "+", "-11", "*", "/", "*", "17", "+", "5", "+"]))