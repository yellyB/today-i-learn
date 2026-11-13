# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        def getCount(root, targetSum):
            if not root: return 0
            cnt = 1 if root.val==targetSum else 0
            return cnt + getCount(root.left, targetSum-root.val) + getCount(root.right, targetSum-root.val)
        
        if not root: return 0
        # 현재 노드의 합계 확인, 왼오 노드를 시작점으로하여 따로 확인
        return getCount(root, targetSum) + self.pathSum(root.left, targetSum) + self.pathSum(root.right, targetSum)
            
