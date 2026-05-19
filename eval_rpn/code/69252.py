def evalRPN(tokens: List[str]) -> int:
    #create empty stack
    stack = []
    #set of the operations
    operations = {"+", "*", "-", "/"}

    for token in tokens:
        if token in operations:
            #second operand (top of stack)
            b = stack.pop()
            #first operand
            a = stack.pop()
            if token == "+":
                stack.append(a + b)
            elif token == "-":
                stack.append(a - b)
            elif token == "*":
                stack.append(a * b)
            elif token == "/":
                #truncate toward 0, not floor
                stack.append(int(a / b))
        else:
            #convert string to int and push onto stack
            stack.append(int(token))
    #final result is only element left
    return stack[0]
            
#Approach: I used a stack to process the token from left to right. I push numbers onto the stack, and when an operator is hit, I pop the two operands, apply the operation, 
#and then push the result. The final value left on the stack is the answer.
#Time complexity: The solution is O(n) where n is the number of tokens, since every token is visited exactly once and all stack operations (push/pop) are O(1).m