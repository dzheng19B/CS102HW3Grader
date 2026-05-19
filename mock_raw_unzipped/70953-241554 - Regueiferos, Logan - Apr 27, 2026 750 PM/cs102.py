def reversepolishnotation ( tokens ):
	stack = []
	i = 0
	while (i < len(tokens)):
		if (tokens[i] == "+"):
			stack.append(stack.pop() + stack.pop())
		elif (tokens[i] == "-"):
			temp = 0
			temp = stack.pop()
			stack.append(stack.pop() - temp)
		elif (tokens[i] == "*"):
			stack.append(stack.pop() * stack.pop())
		elif (tokens[i] == "/"):
			temp = 0
			temp = stack.pop()
			stack.append(stack.pop() / temp)
		else:
			stack.append(float(tokens[i]))
		i+=1
	return stack[0]
print(reversepolishnotation(["1","2","3","/","+"]))