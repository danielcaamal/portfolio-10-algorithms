# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def inorderTraversal(self, root: TreeNode):
        results = []

        if not root:
            return results

        def traverse(current):
            if current.left is not None:
                traverse(current.left)
            results.append(current.val)
            if current.right is not None:
                traverse(current.right)
        
        traverse(root)
        return results