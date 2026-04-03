def is_palindrome_linkedlist(head):
    if not head or not head.next:
        return True

    # Step 1: Find midpoint
    fast, slow = head, head
    while fast and fast.next:
        fast = fast.next.next
        slow = slow.next

    # Step 2: Skip middle node for odd length
    if fast:
        slow = slow.next

    # Step 3: Reverse second half
    prev = None
    curr = slow
    while curr:
        nxt = curr.next
        curr.next = prev
        prev = curr
        curr = nxt

    # Step 4: Compare halves
    left, right = head, prev
    while right:
        if left.val != right.val:
            return False
        left = left.next
        right = right.next

    return True
