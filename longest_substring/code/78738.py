[4]

2) Communication & Collaboration
[3]

3) Implementation & Technical Depth
[4]

4) Team Fit & Working Style
[4]

Final Evaluation
[15/16]
Strong Hire
Final Decision
Showcase strong comprehension of the problem through explaining the problem to the interviewer. Communicated well and how strong reasoning skills. Would recommend for his completeness. 
Candidate Form

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