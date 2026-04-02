def reverse_a_linkedlist(head):
    prev = None
    curr = head

    while curr:
        next_current_node = curr.next
        curr.next = prev
        prev = curr
        curr = next_current_node

    return prev   # new head of reversed list
