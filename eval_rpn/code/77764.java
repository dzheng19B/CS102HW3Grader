public int evalRPN(String[] tokens){
deque<Integer> stack = new deque<>();
for (int i = 0;  i < tokens.length; i++)
{
        String character = tokens[i];
        if(character.equals(“+”))
        {
                int num2 = stack.pop();
                int num1 = stack.pop();
                int result = num1 + num2;
                stack.push(result);
        }
        else if(character.equals(“-”))
        {
                int num2 = stack.pop();
                int num1 = stack.pop();
                int result = num1 - num2;
                stack.push(result);
        }
        else if(character.equals(“*”))
        {
                int num2 = stack.pop();
                int num1 = stack.pop();
                int result = num1 * num2;
                stack.push(result);
        }
        else if(character.equals(“/”))
        {
                int num2 = stack.pop();
                int num1 = stack.pop();
                int result = num1 / num2;
                stack.push(result);
        }
        else
        {
                int num = character.parseInt();
                stack.push(num);
        }
}
return stack.pop();
}