class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        

class LinkedList:
    def __init__(self, value):
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node

        
    def append(self, value):
        new_node = Node(value)
        if self.head == None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        return True
        

    def find_middle_node(self):
      # 1. Initialize two pointers: 'slow' and 'fast', 
      # both starting from the head.
      slow = self.head
      fast = self.head
  
      # 2. Iterate as long as 'fast' pointer and its next 
      # node are not None.
      # This ensures we don't get an error trying to access
      # a non-existent node.
      while fast is not None and fast.next is not None:
          
          # 2.1. Move 'slow' one step ahead.
          # This covers half the distance that 'fast' covers.
          slow = slow.next
          
          # 2.2. Move 'fast' two steps ahead.
          # Thus, when 'fast' reaches the end, 'slow' 
          # will be at the middle.
          fast = fast.next.next
  
      # 3. By now, 'fast' has reached or surpassed the end, 
      # and 'slow' is positioned at the middle node.
      # Return the 'slow' pointer, which points to 
      # the middle node.
      return slow

    def has_loop(self):
      # Floyd's cycle-finding algorithm
      # 1. Initialize two pointers: 'slow' and 'fast', 
      # both starting from the head.
      slow = self.head
      fast = self.head
  
      # 2. Continue traversal as long as the 'fast' pointer 
      # and its next node aren't None.
      # This ensures we don't run into errors trying to 
      # access non-existent nodes.
      while fast is not None and fast.next is not None:
          
          # 2.1. Move 'slow' pointer one step ahead.
          slow = slow.next
          
          # 2.2. Move 'fast' pointer two steps ahead.
          fast = fast.next.next
          
          # 2.3. Check for cycle: If 'slow' and 'fast' meet,
          # it means there's a cycle in the linked list.
          if slow == fast:
              # 2.3.1. If they meet, return True 
              # indicating the list has a loop.
              return True
  
      # 3. If we've gone through the entire list and 
      # the pointers never met, then the list doesn't have a loop.
      return False
    
def find_kth_from_end(ll, k):
    # 1. Initialize two pointers, 'slow' and 'fast', both pointing to the 
    # starting node of the linked list.
    slow = fast = ll.head   
    
    # 2. Move the 'fast' pointer 'k' positions ahead.
    for _ in range(k):
        # 2.1. If at any point during these 'k' movements, the 'fast' 
        # pointer reaches the end of the list, then it means the list 
        # has less than 'k' nodes, and thus, returning None is appropriate.
        if fast is None:
            return None
        
        # 2.2. Move the 'fast' pointer to the next node.
        fast = fast.next
    # 3. Now, move both 'slow' and 'fast' pointers one node at a time until 
    # the 'fast' pointer reaches the end of the list. Since the 'fast' pointer 
    # is already 'k' nodes ahead of the 'slow' pointer, by the time 'fast' 
    # reaches the end, 'slow' will be at the kth node from the end.
    while fast:
        slow = slow.next
        fast = fast.next
        
    # 4. Return the 'slow' pointer, which is now pointing to the kth node 
    # from the end.
    return slow
    
my_linked_list = LinkedList(1)
my_linked_list.append(2)
my_linked_list.append(3)
my_linked_list.append(4)
my_linked_list.append(5)


k = 2
result = find_kth_from_end(my_linked_list, k)

print(result.value)  # Output: 4
