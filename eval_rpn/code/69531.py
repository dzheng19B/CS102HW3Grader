def evalRPN(tokens: List[str] -> int): 
    # [4, 13, 5, /, +]

    # Time Complexity O(n)
    # Space Complexity O(n)

    #5
    #13 /  (2)
    #4 +  = 6 

    #13 / 5 = 2.5 = 2   


    #[result] 

    #result
    #result + 5 
    #result + 17
    #result * 10
    #result / 6
    #result * - 11
    #(3 + 9)

    #results = 0
    #l, r = 0, 1

    operations = {}

    if len(tokens) <= 2:
        return tokens[0]

    while(len(tokens) > 1):
        if tokens[r+1] != "*" || tokens[r+1] != "/" || tokens[r+1] != "+" :
            l++ 
            r++
            continue

        operations.append(tokens[l] + tokens[r+1] + tokens[r]);
        tokens.remove(r)
        tokens.remove(r+1)
        tokens[l] = "x"


    lr, rr, op = 0, 0 , 0
    results = 0
    for i in operations: 
        lr = operations[i][0]
        op = operations[i][1]
        rr = operations[i][2]

        if lr == "x":
            lr = results

        if op == "+":
            result = lr + rr    

        elif op == "*":
    
            result = lr * rr
        elif op == "/":
            result = lr // rr
    
    return results