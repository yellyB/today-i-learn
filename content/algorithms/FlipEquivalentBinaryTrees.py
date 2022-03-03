# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def flipEquiv(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        def isSame(r1, r2):
            # 둘 다 없으면 성공
            if not r1 and not r2:
                return True
            # 둘 중 하나만 없으면 실패
            if not r1 or not r2:
                return False
            if r1.val == r2.val:
                # 왼오를 바꾼경우와 안바꾼 경우 둘다 검사
                return (isSame(r1.left, r2.right) and isSame(r1.right, r2.left)) or (isSame(r1.left, r2.left) and isSame(r1.right, r2.right))
            else:
                return False
        return isSame(root1, root2)
