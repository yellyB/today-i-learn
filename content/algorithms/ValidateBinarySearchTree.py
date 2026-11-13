# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        print(pow(2,31)-1)
        def isValid(root, minVal, maxVal):
            if not root: return True
            if minVal >= root.val or root.val >= maxVal: return False
            return isValid(root.left, minVal, root.val) and isValid(root.right, root.val, maxVal)
        return isValid(root,-pow(2,31)-1,pow(2,31))