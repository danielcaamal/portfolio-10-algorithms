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
            
    def insertion_sort(self):
        if self.length < 2:
            return
        
        sorted_list_head = self.head
        unsorted_list_head = self.head.next
        sorted_list_head.next = None
        
        while unsorted_list_head is not None:
            current = unsorted_list_head
            unsorted_list_head = unsorted_list_head.next
            
            if current.value < sorted_list_head.value:
                current.next = sorted_list_head
                sorted_list_head = current
            else:
                search_pointer = sorted_list_head
                while search_pointer.next is not None and current.value > search_pointer.next.value:
                    search_pointer = search_pointer.next
                current.next = search_pointer.next
                search_pointer.next = current
        
        self.head = sorted_list_head
        temp = self.head
        while temp.next is not None:
            temp = temp.next
        self.tail = temp
    
    def merge(self, other_list):
        current = self.head
        other_current = other_list.head
        dummy = Node(0)
        new_current = dummy
        
        while current is not None and other_current is not None:
            if current.value < other_current.value:
                new_current.next = current
                current = current.next
            else:
                new_current.next = other_current
                other_current = other_current.next
            
            new_current = new_current.next
        
        if current is not None:
            new_current.next = current
            # The tail remains at the last
        else:
            new_current.next = other_current
            self.tail = other_list.tail          
        
        self.head = dummy.next
        self.length = self.length + other_list.length

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

def test_insertion_sort():
    my_linked_list = LinkedList(4)
    my_linked_list.append(2)
    my_linked_list.append(6)
    my_linked_list.append(5)
    my_linked_list.append(1)
    my_linked_list.append(3)

    print("Linked List Before Sort:")
    my_linked_list.print_list()

    my_linked_list.insertion_sort()

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

def test_merge_sort():
    l1 = LinkedList(1)
    l1.append(3)
    l1.append(5)
    l1.append(7)


    l2 = LinkedList(2)
    l2.append(4)
    l2.append(6)
    l2.append(8)

    l1.merge(l2)

    l1.print_list()


    """
        EXPECTED OUTPUT:
        ----------------
        1 
        2 
        3 
        4 
        5 
        6 
        7
        8

    """

if __name__ == "__main__":
    # test_bubble_sort()
    # test_selection_sort()
    # test_insertion_sort()
    test_merge_sort()