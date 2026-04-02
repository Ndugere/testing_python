def remove_linklist_elements(head, element_to_remove):
    prev = None
    current_node = head
    while current_node:
        if current_node.val == element_to_remove and current_node == head:
            head = current_node.next
        elif current_node.val == element_to_remove and current_node != head:
            prev.next = current_node.next
        else:
            prev = current_node
        
        current_node = current_node.next
    return head
