class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class Queue:
    def __init__(self, value):
        self.first = Node(value)
        self.last = self.first
        self.length = 1
    
    def enqueue(self, value):
        new_node = Node(value)
        
        if self.length == 0:
            self.first = new_node
            self.last = new_node
            self.length = 1
            return True
        
        self.last.next = new_node
        self.last = new_node
        self.length += 1
        return True
    
    def dequeue(self):
        if self.length == 0:
            return None
        
        if self.length == 1:
            self.first = None
            self.last = None
            return True
        
        temp = self.first
        self.first = self.first.next
        temp.next = None
        self.length += 1
        return temp
        