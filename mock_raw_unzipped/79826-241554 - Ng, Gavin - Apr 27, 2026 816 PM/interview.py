from typing import List

def evalRPN(tokens: List[str]) -> int:
    sum = 0
    stack = []
 
    for i in range(len(tokens)):
        if tokens[i] == "+" or tokens[i] == "-" or tokens[i] == "*" or tokens[i] == "/": #checks if token is an operator
            num2 = stack.pop()#pops the 2 operands
            num1 = stack.pop()
            if tokens[i] == "+": 
                sum = num1 + num2
            elif tokens[i] == "-":
                sum = num1 - num2
            elif tokens[i] == "*":
                sum = num1 * num2
            else:
                sum = int(num1 / num2) #else divides already checked is operator
            stack.append(sum) #push the result back to stack
        else:
            stack.append(int(tokens[i])) #else pushes next token to stack as int

    return stack.pop() #last element would be final answer




print(evalRPN(["2", "1", "+", "3", "*"])) #sol: 9 
print(evalRPN(["4", "13", "5", "/", "+"])) #sol: 6
print(evalRPN(["10", "6", "9", "3", "+", "-11", "*", "/", "*", "17", "+", "5", "+"])) #sol: 22 (did math on paper)