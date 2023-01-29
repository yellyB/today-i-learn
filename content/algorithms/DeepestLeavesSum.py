# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deepestLeavesSum(self, root: Optional[TreeNode]) -> int:
        res = 0
        q = [root]
        while q:
            res = 0
            temp = []
            while q:
                node = q.pop()
                res += node.val
                if node.left: temp.append(node.left)
                if node.right: temp.append(node.right)
            q = temp[:]
        return res
