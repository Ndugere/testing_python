class Node:
    def __init__(self, data):
        self.data = data 
        self.next = None

class Queue:
    def __init__(self):
        self.front = None
        self.rear = None
        self.size = 0
    
    def enqueue(self, element):
        new_node = Node(element)
        if self.rear is None:
            self.front = self.rear = new_node
            self.size += 1
            return
        else:
            self.rear.next = new_node
            self.rear = new_node
            self.size += 1



