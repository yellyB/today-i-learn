# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumEvenGrandparent(self, root: TreeNode) -> int:
        nodes = [(root,1,1)]  # root, 엄빠, 할   / 첨엔 없으니까 걍 홀수인 1로
        sums = 0
        while nodes:
            curr = nodes.pop()
            node = curr[0]
            if node:
                if curr[2]%2==0:
                    sums += node.val
                nodes.append((node.left, node.val, curr[1]))
                nodes.append((node.right, node.val, curr[1]))
            
        return sums
