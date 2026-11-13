# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
        rest = []  # 타겟에서 뺀 남은 숫자 저장
        stack = [root]
        while stack:
            node = stack.pop()
            if node:
                if node.val in rest:
                    return True
                else:
                    rest.append(k - node.val)
                stack.append(node.left)
                stack.append(node.right)
        return False