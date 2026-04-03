class Node:
    def __init__(self, val):
        self.val = val
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def remove_nodes_with_value(self, val):
        dummy_head = Node(None)
        dummy_head.next = self.head
        current_node = dummy_head

        while current_node and current_node.next:
            if current_node.next.val == val:
                current_node.next = current_node.next.next
            else:
                current_node = current_node.next
        self.head = dummy_head.next
