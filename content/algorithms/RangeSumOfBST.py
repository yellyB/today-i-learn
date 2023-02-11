# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        def dfs(node, val):
            if not node:
                return val
            
            res = 0
            if low <= node.val <= high:
                res += node.val
            if low < node.val:
                res += dfs(node.left, val)
            if node.val < high:
                res += dfs(node.right, val)
            
            return val+res

        return dfs(root, 0)
