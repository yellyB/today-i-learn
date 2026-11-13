# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        def left(root):
            sums = 0
            if not root: return 0
            if not root.left and not root.right:
                return root.val
            if root.left:
                sums += left(root.left)
            if root.right:
                sums += right(root.right)
            return sums
        
        def right(root):
            sums = 0
            if not root: return 0
            if root.left:
                sums += left(root.left)
            if root.right:
                sums += right(root.right)
            return sums
            
        sums = 0
        if root.left: sums += left(root.left)
        if root.right: sums += right(root.right)
        return sums
            
#         sums = 0
        
#         while root:
#             if root.left:
#                 sums += left(root.left)
#             root = root.right
        
        
#         return sums
