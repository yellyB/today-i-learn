# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pruneTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        def dfs(root):
            if not root:
                return None
            
            root.left = dfs(root.left)
            root.right = dfs(root.right)
            
            # 값이 0일때 왼, 오 가 값이 없으면(0이 있었으면 그 전에 지워졌을거임)
            if root.val == 0 and root.left == None and root.right == None:
                return None
            else:
                return root
        
        return dfs(root)
