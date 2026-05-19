1) Problem Understanding (4)
-understood completely
-explained approach

2) Communication & Collaboration (3)
-asked for clarification when typing code
-adapted quickly to the feedback
-drew out his thought process

3) Implementation & Technical Depth (4)
-explained the complexities
-code works

4) Team Fit & Working Style(4)
-didn't complain
-remained calm 
-didn't stress out

Final Evaluation 15/16
Hire

Final Decision
He immediately explained his through process when hearing the problem and even drew it out. However, he got a little confused with the code which I helped clarify leading to the code working. I made my decision to hire him because he knew what he was doing and worked together with me when he was confused.

Candidate Form

def exalRPN(tokens: List[str]):
    arr=[]
    
    for i in tokens:
        if i == "+":
            arr.append(arr.pop() + arr.pop())
        elif i == "*":
            arr.append(arr.pop() * arr.pop())
        elif i == "/":
            second = arr.pop()
            first = arr.pop()
            arr.append(int(first / second))
        elif i == "-":
            second = arr.pop()
            first = arr.pop()
            arr.append(first - second)
        else:
            arr.append(int(i))
        return arr[0]