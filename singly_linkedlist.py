class Node:
    """A node in a singly linked list."""
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    """A simple singly linked list implementation."""
    def __init__(self):
        self.head = None
        self.length = 0

    def prepend(self, data):
        """Insert a new node at the beginning (O(1))."""
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node
        self.length += 1

    def append(self, data):
        """Insert a new node at the end (O(n))."""
        new_node = Node(data)
        if not self.head:
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node
        self.length += 1

    def delete(self, value):
        """Delete the first node with the given value (O(n))."""
        if not self.head:
            raise ValueError("Value not found in list")

        if self.head.data == value:
            self.head = self.head.next
            self.length -= 1
            return

        current = self.head
        while current.next:
            if current.next.data == value:
                current.next = current.next.next
                self.length -= 1
                return
            current = current.next

        raise ValueError("Value not found in list")

    def __len__(self):
        return self.length

    def __iter__(self):
        """Allow iteration over the list."""
        current = self.head
        while current:
            yield current.data
            current = current.next
            
    def __repr__(self):
        """
        Traverse the list and return a string representation (O(n)).
        """
        nodes = []
        current_node = self.head
        while current_node:
            if current_node is self.head:
                nodes.append(f"Head: -> [{current_node.data}]")
            elif current_node.next is None:
                nodes.append(f"-> Tail: [{current_node.data}]")
            else:
                nodes.append(f"-> [{current_node.data}]")
            current_node = current_node.next
        return "".join(nodes)
