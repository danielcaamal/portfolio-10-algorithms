class Node:
    def __init__(self, value):
        self.value = value
        self.right = None
        self.left = None


class BinarySearchTree:
    def __init__(self):
        self.root = None
        
    
    def insert(self, value):
        new_node = Node(value)
        
        if not self.root:
            self.root = new_node
            return True
        
        temp = self.root
        while True:
            if new_node.value == temp.value:
                return False
            elif new_node.value < temp.value:
                if temp.left is None:
                    temp.left = new_node
                    return True
                else:
                  temp = temp.left
            elif new_node.value > temp.value:
                if temp.right is None:
                    temp.right = new_node
                    return True
                else:
                  temp = temp.right
    
    def contains(self, value):
        temp = self.root
        
        while temp:
            if value == temp.value:
                return True
            elif value < temp.value:
                temp = temp.left
            elif value > temp.value:
                temp = temp.right
        return False