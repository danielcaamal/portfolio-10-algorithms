
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeTwoLists(self, list1: ListNode, list2: ListNode) -> ListNode:
        current = list1
        other_current = list2
        dummy = ListNode(0)
        current_dummy = dummy

        while current is not None and other_current is not None:
            if current.val < other_current.val:
                current_dummy.next = current
                current = current.next
            else:
                current_dummy.next = other_current
                other_current = other_current.next
            
            current_dummy = current_dummy.next
        
        self.print(dummy)
    
        if current is not None:
            current_dummy.next = current
        else:
            current_dummy.next = other_current

        return dummy.next
      
    
    def print(self, list1):
        array = []
        while list1 is not None:
            array.append(list1.val)
            list1 = list1.next
        
        print(array)

                
        

if __name__ == "__main__":
    node1_1 = ListNode(1)
    node1_1.next = ListNode(2)
    node1_1.next.next = ListNode(4)
    
    node2_1 = ListNode(1)
    node2_1.next = ListNode(3)
    node2_1.next.next = ListNode(4)
    
    solution = Solution()
    result = solution.mergeTwoLists(node1_1, node2_1)
    solution.print(result)
    
    