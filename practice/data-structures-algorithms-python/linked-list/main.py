class Node:
  def __init__ (self, value):
    self.value = value
    self.next = None


class LinkedList:
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
    if self.head is None:
      self.head = new_node
      self.tail = new_node
      self.length = 1
      return self
    
    self.tail.next = new_node
    self.tail = new_node
    self.length += 1
    return self
  
  def pop(self):
    if self.length == 0:
      return None
    
    temp = self.head
    pre = self.head
    while temp.next is not None:
      pre = temp
      temp = temp.next
    
    self.tail = pre
    self.tail.next = None
    self.length -= 1
    
    if self.length == 0:
      self.head = None
      self.tail = None
    
    return temp
  
  def prepend(self, value):
    new_node = Node(value)
    
    if self.length == 0:
      self.head = new_node
      self.tail = new_node
      self.length = 1
      return self
    
    new_node.next = self.head
    self.head = new_node
    self.length += 1
    return self
  
  def pop_first(self):
    if self.length == 0:
      return None
    
    temp = self.head
    self.head = self.head.next
    temp.next = None
    self.length -= 1
    
    if self.length == 0:
      self.tail = None
    
    return temp
  
  def get(self, index):
    if index < 0 or index >= self.length:
      return None
    
    temp = self.head
    for _ in range(index):
      temp = temp.next
      
    return temp
  
  
  def set_value(self, index, value):
    node = self.get(index)
    
    if node:
      node.value = value
      return node
    
    return None
  
  
  def insert(self, index, value):
    if index < 0 or index > self.length:
      return None
    
    if index == 0:
      return self.prepend(value)
    
    if index == self.length:
      return self.append(value)
    
    new_node = Node(value)
    temp = self.get(index - 1)
    
    new_node.next = temp.next
    temp.next = new_node
    self.length += 1
    return self
  
  
  def remove(self, index):
    
    if index < 0 or index > self.length - 1:
      return None
    
    if index == 0:
      return self.pop_first()
    
    if index == self.length - 1:
      return self.pop()
    
    temp = self.get(index - 1)
    deleted = temp.next
    temp.next = deleted.next
    deleted.next = None
    self.length =- 1
    return deleted
    
  def reverse(self):
    temp = self.head
    self.head = self.tail
    self.tail = temp
    before = None
    after = temp.next
    
    for _ in range(self.length):
      after = temp.next
      temp.next = before
      before = temp
      temp = after
    
    
    
    
    
    
    
    
if __name__ == "__main__":
  my_linked_list = LinkedList(1)
  my_linked_list.append(2)
  my_linked_list.pop()
  my_linked_list.pop()
  my_linked_list.pop()
  my_linked_list.append(2)
  my_linked_list.append(3)
  my_linked_list.append(4)
  my_linked_list.prepend(1)
  my_linked_list.prepend(0)
  my_linked_list.pop_first()
  my_linked_list.pop_first()
  my_linked_list.pop_first()
  my_linked_list.set_value(1, 2)
  my_linked_list.insert(1,1)
  my_linked_list.print_list()
  my_linked_list.reverse()
  my_linked_list.print_list()