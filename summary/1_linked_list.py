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
        self.length += 1
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
    
    def _swap(self, node1, node2):
        temp = node1.value
        node1.value = node2.value
        node2.value = temp
    
    def bubble_sort(self):
        if self.length < 2:
            return
        
        for i in range(self.length - 1, 0, -1):
          current = self.head
          j = 0
          while current.next is not None and j < i:
              if current.value > current.next.value:
                  self._swap(current, current.next)
              current = current.next
              j += 1
        
    def selection_sort(self):
        if self.head is None:
            return
        if self.length < 2:
            return
        start_node = self.head
        for i in range(self.length - 1):
            current = start_node
            smallest = current
            while current is not None:
                if current.value < smallest.value:
                    smallest = current
                current = current.next
              
            if smallest != start_node:
                self._swap(start_node, smallest)
            start_node = start_node.next

def test_bubble_sort():
    my_linked_list = LinkedList(4)
    my_linked_list.append(2)
    my_linked_list.append(6)
    my_linked_list.append(5)
    my_linked_list.append(1)
    my_linked_list.append(3)

    print("Linked List Before Sort:")
    my_linked_list.print_list()

    my_linked_list.bubble_sort()

    print("\nSorted Linked List:")
    my_linked_list.print_list()



    """
        EXPECTED OUTPUT:
        ----------------
        Linked List Before Sort:
        4
        2
        6
        5
        1
        3

        Sorted Linked List:
        1
        2
        3
        4
        5
        6

    """
    
def test_selection_sort():
    my_linked_list = LinkedList(4)
    my_linked_list.append(2)
    my_linked_list.append(6)
    my_linked_list.append(5)
    my_linked_list.append(1)
    my_linked_list.append(3)

    print("Linked List Before Sort:")
    my_linked_list.print_list()

    my_linked_list.selection_sort()

    print("\nSorted Linked List:")
    my_linked_list.print_list()



    """
        EXPECTED OUTPUT:
        ----------------
        Linked List Before Sort:
        4
        2
        6
        5
        1
        3

        Sorted Linked List:
        1
        2
        3
        4
        5
        6

    """


if __name__ == "__main__":
    # test_bubble_sort()
    test_selection_sort()