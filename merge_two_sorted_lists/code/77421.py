def mergeTwoList(list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
    curr1 = list1
    curr2 = list2
    if list1 == None and list2 == None:
        return None
    elif list1 == None:
        return list2
    elif list2 == None:
        return list1
    while curr1 and curr2:
        if curr1.val <= curr2.val and curr1.next == None:
            curr1.next = curr2
            curr2 = curr2.next
        if curr1.val <= curr2.val and curr1.next != None and curr2.val < curr1.next.val:
            temp = curr1.next
            curr1.next = curr2
            curr2 = curr2.next
            curr1.next.next = temp
        curr1 = curr1.next
    return list1