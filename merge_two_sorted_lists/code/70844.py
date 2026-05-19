Time complexity of my problem: O(n+m)
My solution goes through each of the lists completely and since the lists aren't identical, we have list1 of length n and list2 of length m. We compare each of the values and then go through until no more left to search and then return the head. We choose the head of the list that has a bigger value and then we move the pointer and keep repeating until the comparison is done. 


def mergeTwoLists(list1: Optional[ListNode], list2: Optional[ListNode]) -> optional[ListNode]:
    x = listNode()
    curr = x

    while list1 and list2 != null:
        if list1.val <= list2.val:
            curr.next = list1
            list1 = list1.next
        elif list1.val >= list2.val:
            curr.next = list2
            list2 = list2.next
        curr = curr.next

    return x