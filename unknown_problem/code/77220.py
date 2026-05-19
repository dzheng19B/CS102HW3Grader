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