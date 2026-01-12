from single_link_list import Linkedlist

def merge_sort_for_a_linked_list(linked_list):
    if linked_list.size() == 1 or linked_list.head is None:
        return linked_list
    left_linked_list, right_linked_list = split_linked_list(linked_list)
    left = merge_sort_for_a_linked_list(left_linked_list)
    right =merge_sort_for_a_linked_list(right_linked_list)

    return merge(left, right)

def split_linked_list(linked_list):
    if linked_list.head == None or not linked_list:
        left_linked_list = linked_list
        right_linked_list = None
        return left_linked_list, right_linked_list
    mid = linked_list.size() //2
    mid_node = linked_list.node_at_index(mid - 1)

    left_linked_list = linked_list
    right_linked_list = Linkedlist()
    right_linked_list.head = mid_node.next
    mid_node.next = None
    return left_linked_list, right_linked_list


def merge(left, right):
    sorted_linked_list = Linkedlist()
    sorted_linked_list.add(10)
    current_node = sorted_linked_list.head
    left_head = left.head
    right_head = right.head

    while left_head or right_head:
        if left_head is None:
            current_node.next = right_head
            right_head = right_head.next
        elif right_head is None:
            current_node.next = left_head
            left_head = left_head.next
        else:
            left_data = left_head.data
            right_data = right_head.data

            if left_data < right_data:
                current_node.next = left_head
                left_head = left_head.next

            else:
                current_node.next = right_head
                right_head= right_head.next
        current_node = current_node.next

    real_head = sorted_linked_list.head.next

    sorted_linked_list.head = real_head

    return sorted_linked_list

l = Linkedlist()

l.add(7)
l.add(10)
l.add(2)

print(l)

print(merge_sort_for_a_linked_list(l))



