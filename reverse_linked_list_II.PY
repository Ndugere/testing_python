class Node:
    def __init__(self, val):
        self.val = val
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None


def reverse_linked_list(head, left_pointer, right_pointer):
    dum_head = Node(None)
    dum_head.next = head

    current_node = dum_head
    count = 1

    # Step 1: move to node BEFORE left_pointer
    while current_node and count < left_pointer:
        current_node = current_node.next
        count += 1

    if not current_node or not current_node.next:
        return dum_head.next

    # Step 2: mark important nodes
    tail_of_first_node = current_node
    second_head = current_node.next

    # Step 3: reverse sublist
    prev = None
    second_node = second_head

    steps = right_pointer - left_pointer + 1

    while second_node and steps > 0:
        next_node = second_node.next
        second_node.next = prev
        prev = second_node
        second_node = next_node
        steps -= 1

    # Step 4: reconnect
    tail_of_first_node.next = prev
    second_head.next = second_node

    return dum_head.next