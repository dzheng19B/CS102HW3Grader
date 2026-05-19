mergeTwoLists(list1:
 
Optional[ListNode],
 
list2:
 
Optional[ListNode])
 
->
 
Optional[ListNode]:
 
 
newList
 
=
 
ListNode()
 
 
currNode
 
=
 
newList
  
 
while
 
list1
 
and
 
list2
 
!=
 
NULL:
 
 
 
if
 
list1.val
 
>
 
list2.val:
 
 
 
 
newList.next
 
=
 
list2
 
 
 
 
list2
 
=
 
list2.next
 
 
 
else:
 
 
 
 
newList.next
 
=
 
list1
 
 
 
 
list1
 
=
 
list1.next
 
 
 
 
currNode
 
=
 
currNode.next
 
 
 
 
if
 
list1:
 
 
 
 
currNode
 
=
 
list1.next
 
 
 
else:
 
 
 
 
currNode
 
=
 
list2.next
 
 
 
return
 
newList