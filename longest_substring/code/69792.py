2) Communication & Collaboration
4

3) Implementation & Technical Depth
4

4) Team Fit & Working Style
4

Final Evaluation
15/16

Final Decision
Hire

Candidate Form

def mergeTwoLists(list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
    #base cases so if these are none, I can just return the other list and save memory
    if list1 is None:
        return list2
    if list2 is None:
        return list1
    #if the value of list1 is less than or equal to list 2, recursively call the function
    #Set list1.next to the merged result of the remaining nodes.
    #Return list1 as the current head.
    if list1.val <= list2.val:
        list1.next = self.mergeTwoLists(list1.next, list2)
        return list1
    #do the same with list2
    else: 
        list2.next = self.mergeTwoLists(list2.next, list1)
        return list2