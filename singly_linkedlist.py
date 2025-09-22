class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Linkedlist:
    def __init__(self):
        self.head = None
        self.length = 0

    def prepend(self, data):
        """
        This method prepend a new node in the front of the list like a stack
        """
        new_node = Node(data)
        if self.head is not None:
            new_node.next = self.head
        self.head = new_node
        self.length += 1
    
    def isEmpty(self):
        """
        returns true if the lenght of the list is zero i.e if empty
        this operation is O(1)
        """
        return self.length == 0
    
    def post_pend(self, data):
        """
        This method append the a new node at the end of the list
        this operation is O(n)
        """
        if self.isEmpty():
            self.prepend(data)
        else:
            new_node = Node(data)
            current_node = self.head
            while current_node.next:
                current_node = current_node.next
            current_node.next = new_node
            self.length += 1

