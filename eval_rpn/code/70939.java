evalRPN(String[]
 
tokens)
 
{
 
 
stack<Integers>
 
token2
 
=
 
new
 
Stack<>();
 
 
 
 
for
 
(String
 
x
 
:
 
tokens)
 
{
 
 
 
if
 
(x.equals("+"))
 
{
  
 
 
token2.push(token2.pop()
 
+
 
token2.pop());
 
 
 
}
 
 
else
 
if
 
(x.equals("-"))
 
{
 
 
 
 
int
 
two
 
=
 
token2.pop();
 
 
 
 
 
int
 
one
 
=
 
token2.pop();
 
 
 
 
token2.push(one
 
-
 
two);
 
 
 
}
 
 
else
 
if
 
(x.equals("*"))
 
{
 
 
 
 
token2.push(token2.pop()
 
*
 
token2.pop());
 
 
 
}
 
 
else
 
if
 
(x.equals("/"))
 
{
 
 
 
 
int
 
two
 
=
 
token2.pop();
 
 
 
 
int
 
one
 
=
 
token2.pop();
 
 
 
 
token2.push(one/two);
 
 
}
 
}
 
 
 
return
 
token2.peek();
 
 
}