def mergeTwoLists(list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
    #will be ediiting list 1
    #head = list1
    #prev = temp value

    #while list2:
        #if val2 is than val1, set the next node to be the node in list1, update previous or head value if necessesary

    if not list1 and not list2:
        return None
    if not list1:
        return list2
    if not list2:
        return list1
    
    head = list1            #1 - 2- 4
    prev = None

    while list2 and list1:       
        if list2.val <= list1.val:               
            list2.next = list1                
            if prev is None:
                head = list2                #1 -1 -2- 4
                prev = list2
            else:
                prev.next = list2
                prev = prev.next
                list2 = list2.next
        else:
            list1 = list1.next
            prev = prev.next
    

    while list2:
        prev.next = list2
        prev = prev.next

    return head



 # The time complexity of my code is O(n) because it iterates through each loop at least once, say the length of list1 is n an list2 is m the time complexity would be O(n + m) which is the same as linear time and 0(n)
 # The space complexity of my code is O(1) because no new objects are created therefore constant space is used
 # My solution is a two pointer solution that updates list one based on the value of list2. if the value of list2 is less than or equal 2 my code updates the previous node to point to the list2 node and the list2 node points to the current list1 pointer. the list2 pointer is moved forward
 # if list2 value is greater than the list 1 pointer the list 1 pointer is moved forward and the prev node is updated.
 # basically it insterts the list2 nodes in the correct spot of list1

 # My interviewer guided me a little with edge cases and other small errors, did not feel antagonized.
     