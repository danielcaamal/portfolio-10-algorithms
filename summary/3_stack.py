class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
    
    
class Stack:
    def __init__(self, value):
        new_node = Node(value)
        self.top = new_node
        self.height = 1
        
    def push(self, value):
        new_node = Node(value)
        new_node.next = self.top
        self.top = new_node
        self.height += 1
    
    def pop(self):
        if self.height == 0:
            return None
          
        if self.height == 1:
            temp = self.top
            self.top = None
            return temp
        
        temp = self.top
        self.top = temp.next
        self.height -= 1
        return temp
    
    