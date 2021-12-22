# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        result = []
        stack = [root]
        while stack:
            node = stack.pop()
            if node:
                result.append(node.val)  # 맨 나중에 올 거 먼저 넣음(반대순서로 출력할거니까)
                stack.append(node.left)  # 왼쪽이 맨 첨에 와야함. 근데 반대순서로 할거니까 먼저 넣어서 나중에 나오도록
                stack.append(node.right)
        return result[::-1]