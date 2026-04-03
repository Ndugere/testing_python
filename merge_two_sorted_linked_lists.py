class Node:
    def __init__(self, val):
        self.val =val
        self.next = None
def merge_two_sorted_linked_lists(list1, list2):
    dummy_head = Node(None)
    list1_current_node= list1.head
    list2_current_node=list2.head

    while list1_current_node and list2_current_node:
        if list1_current_node.val < list2_current_node.val:
            dummy_head.next = list1_current_node
            list1_current_node = list1_current_node.next
        else:
            dummy_head.next = list2_current_node
            list2_current_node = list2_current_node.next
        dummy_head = dummy_head.next
    if list1_current_node or list2_current_node:
        dummy_head.next = list1_current_node if list1_current_node else list2_current_node
    
    return dummy_head.next

        
