def evalRPN(tokens: List[str]) -> int:
    tack = []
    num1 = 0 
    num2 = 0
    for bench in tokens:
        if bench == “+”:
            num1 = tack.pop()
            num2 = tack.pop()
            tack. append(num1+num2)
        elif bench == “-”:
            num1 = tack.pop()
            num2 = tack.pop()
            tack. append(num1-num2)
        elif bench == “/”:
            num1 = tack.pop()
            num2 = tack.pop()
            tack. append(num1/num2)
        elif bench == “*”:
            num1 = tack.pop()
            num2 = tack.pop()
            tack.append(num1*num2)
        else:
            tack.append(int(bench)) #if the element is not an operator, it can be cast to an int.
    return tack.pop()
#explanation on paper.
#Stack of encountered numbers - String array
#When we hit an operator, we condense the last 2 numbers into their result and add it back into the stack.
#repeat until end of array, where stack size = 1. Return int value.

#Edge cases are safe: min size is 1 and a valid arithmetic operation is guaranteed