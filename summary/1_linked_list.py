class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self, value):
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        self.length = 1
    
    def print_list(self):
        current = self.head
        while current is not None:
            print(current.value)
            current = current.next
            
    def append(self, value):
        new_node = Node(value)
        
        if self.length == 0:
            self.tail = new_node
            self.head = new_node
            self.length = 1
            return True
        
        self.tail.next = new_node
        self.tail = new_node
        return True
    
    def pop(self):
        if self.length == 0:
            return None
        
        current = self.head
        prev = self.head
        
        while current.next:
            prev = current
            current = current.next
        
        self.tail = prev
        self.tail.next = None
        self.length -= 1
        
        if self.length == 0:
            self.head = None
            self.tail = None
    
        return current

    def prepend(self, value):
        new_node = Node(value)
        
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
            self.length = 1
            return True
        
        new_node.next = self.head
        self.head = new_node
        self.length += 1
        return True
    
    
    def pop_first(self):
        if self.length == 0:
            return None
        
        current = self.head
        self.head = self.head.next
        current.next = None
        self.length -= 1
        
        if self.length == 0:
            self.head = None
            self.tail = None
        
        return current

    def get(self, index):
        if index < 0 or index >= self.length:
            return None
        
        current = self.head
        
        for _ in range(index):
            current = current.next
        
        return current
      
    
    def set(self, index, value):
        current = self.get(index)
        
        if not current:
            return None
        
        current.value = value
        return True
      

    def insert(self, index, value):
        if index < 0 or index > self.length:
            return None
        
        if index == 0:
            return self.prepend(value)
        
        if index == self.length:
            return self.append(value)
        
        new_node = value
        prev = self.get(index - 1)
        new_node.next = prev.next
        prev.next = new_node
        self.length += 1
        return True
      
    
    def remove(self, index):
        if index < 0 or index >= self.length:
            return None
        
        if index == 0:
            return self.pop_first()
        
        if index == self.length - 1:
            return self.pop()
        
        prev = self.get(index - 1)
        current = prev.next
        prev.next = current.next
        current.next = None
        self.length -= 1
        return True
      
    
    def reverse(self):
        temp = self.head
        self.head = self.tail
        self.tail = temp
        after = temp.next
        before = None
        
        for _ in range(self.length):
            after = temp.next
            temp.next = before
            before = temp
            temp = after
        