class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class Linklist:
    def __init__(self):
        self.head = None

    def add(self, value):
        new_node = Node(value)
        new_node.next = self.head
        self.head = new_node
    
    def size(self):
        count = 0
        current_node = self.head
        while current_node:
            count += 1
            current_node = current_node.next
        return count
    
    def is_empty(self):
        return self.head is None
        
    def insert(self, index, value):
        if index == 0:
            self.add(value)
            return True

        new_node = Node(value)
        current_node = self.head
        count = 0

        while current_node:
            if count == index - 1:
                new_node.next = current_node.next
                current_node.next = new_node
                return True

            current_node = current_node.next
            count += 1

        return False
    
    def if_exist(self, value):
        current_node = self.head
        while current_node:
            if current_node.data == value:
                return True
            current_node = current_node.next
        return False
        
    def __repr__(self):
        linklist = []
        current_node = self.head
        while current_node:
            if current_node == self.head:
                linklist.append(f"[Head]:{current_node.data}")
            elif not current_node.next:
                linklist.append(f"[Tail]:{current_node.data}")
            else:
                linklist.append(str(current_node.data))
            current_node = current_node.next
        return " -> ".join(linklist)
