# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getAllElements(self, root1: TreeNode, root2: TreeNode) -> List[int]:
        vals = []
        def getVals(root):
            if root:
                vals.append(root.val)
                getVals(root.left)
                getVals(root.right)
            return
        
        getVals(root1)
        getVals(root2)
        
        vals.sort()
        
        
        
        return vals
