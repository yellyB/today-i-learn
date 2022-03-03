# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        def getCount(root, currMax):
            if not root: return 0
            cnt = 1 if root.val >= currMax else 0  # 현 max보다 크다? 최종결과에 1 더해줄거
            currMax = max(currMax, root.val)
            return getCount(root.left, currMax) + getCount(root.right, currMax) + cnt
        
        return getCount(root, root.val)
    
