# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        def recursion(root):
            if not root: return False
            
            left = recursion(root.left)
            right = recursion(root.right)
            
            mid = root == p or root == q
            
            if mid + left + right >= 2:
                return root
            
            return mid or left or right
            
            return
        
        
        return recursion(root)
