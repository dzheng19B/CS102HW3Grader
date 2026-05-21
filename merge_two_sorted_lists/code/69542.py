def mergeTwoLists(list1, list2):
    dummy = ListNode()
    current = dummy
    while list1 and list2:
        if list1.val > list2.val:
            current.next = list2
            list2 = list2.next
        if list1.val < list2.val:
            current.next = list1
            list1 = list1.next
        current = current.next
    if list1:
        while list1:
            current.next = list1
            list1 = list1.next
            current = current.next
    if list2:
        while list2:
            current.next = list2
            list2 = list2.next
            current = current.next
    return dummy.next
