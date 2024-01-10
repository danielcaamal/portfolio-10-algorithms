class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None


class DoublyLinkedList:
    def __init__(self, value):
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        self.length = 1
    
    
    def print_list(self):
        temp = self.head
        while temp is not None:
            print(temp.value)
            temp = temp.next
    
    
    def append(self, value):
        new_node = Node(value)
        
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
            self.length = 1
            return True
        
        self.tail.next = new_node
        new_node.prev = self.tail
        self.tail = new_node
        self.length += 1
        return True
    
    def pop(self):
        if self.length == 0:
            return None
        
        if self.length == 1:
            temp = self.head
            self.head = None
            self.tail = None
            return temp

        temp = self.tail
        temp.prev.next = None
        self.tail = temp.prev
        temp.prev = None
        self.length -= 1
        return temp
      
    def prepend(self, value):
        new_node = Node(value)
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
            self.length += 1
            return True
        
        new_node.next = self.head
        self.head.prev = new_node
        self.head = new_node
        self.length += 1
        return True
      
    def pop_first(self):
        if self.length == 0:
            return None
        
        if self.length == 1:
            temp = self.head
            self.head = None
            self.tail = None
            self.length = 0
            return temp
        
        temp = self.head
        self.head = self.head.next
        self.prev = None
        temp.next = None
        self.length -= 1
        return temp
      
    
    def get(self, index):
        if index < 0 or index >= self.length:
            return None
        
        temp = self.head
        
        if index < self.length / 2:
            for _ in range(index):
                temp = temp.next
        else:
            temp = self.tail
            for _ in range(self.length - 1, index, -1):
                temp = temp.prev
        
        return temp
    
    
    def set(self, index, value):
        current = self.get(index)
        
        if current is None:
            return None
        
        current.value = value
        return True
    
    
    def insert(self, index, value):
        if index < 0 or index >= self.length:
            return None
        
        if index == 0:
            return self.prepend(value)
        if index == self.length:
            return self.append(value)
        
        new_node = Node(value)
        before = self.get(index)
        after = before.next
        new_node.prev = before
        new_node.next = after
        before.next = new_node
        after.prev = new_node
        self.length += 1
        return True
        
    def remove(self, index):
        if index < 0 or index > self.length:
            return None
        
        if index == 0:
            return self.pop_first()
        if index == self.length - 1:
            return self.pop()
        
        current = self.get(index)
        current.prev.next = current.next
        current.next.prev = current.prev
        self.length -= 1
        return current
    
    