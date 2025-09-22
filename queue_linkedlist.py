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
        else:
            self.rear.next = new_node
            self.rear = new_node
        self.size += 1
    
    def dequeue(self):
        if self.is_empty():
            return "Queue is empty"
        temp = self.front

        self.front = self.front.next
        self.size -= 1

        if self.front is None:
            self.rear = None
        return temp.data
    
    def peek(self):
        if self.is_empty():
            return "Queue is empty"
        return self.front.data
    
    def is_empty(self):
        return self.size == 0
    
    def size_of_queue(self):
        return self.size
    
    def print_queue(self):
        temp = self.front

        while temp:
            print(temp.data, end="-> ")
            temp = temp.next
        print()
