def mergeTwoLists(list1, list2): 
    # changed the function parameters because its easier for me to follow
        dummy = ListNode(0)
        current = dummy
    
        while list1 and list2:
            if list1.val <= list2.val:
                current.next = list1
                list1 = list1.next
            else:
                current.next = list2
                list2 = list2.next
            current = current.next
        #now ill attach remaining list
        current.next = list1 if list1 else list2
    
        return dummy.next