# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def removeLeafNodes(self, root: Optional[TreeNode], target: int) -> Optional[TreeNode]:
        # 814 문제 (https://leetcode.com/problems/binary-tree-pruning/) 랑 매우 비슷
        def dfs(root):
            if not root:
                return None
            
            root.left = dfs(root.left)
            root.right = dfs(root.right)
            
            # 맨 끝이면서 타겟과 같은 값인지 판단
            if not root.left and not root.right and root.val == target:
                root = None
            
            return root//
        
        return dfs(root)