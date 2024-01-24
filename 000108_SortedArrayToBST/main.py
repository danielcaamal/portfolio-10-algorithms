# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        def traverse_arr(arr):
            if len(arr) == 0:
                return None
            mid = (len(arr) - 1) // 2
            node = TreeNode(arr[mid])
            node.left = traverse_arr(arr[:mid])
            node.right = traverse_arr(arr[mid+1:])
            return node
        
        return traverse_arr(nums)

