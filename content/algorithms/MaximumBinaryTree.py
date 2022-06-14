# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def constructMaximumBinaryTree(self, nums: List[int]) -> Optional[TreeNode]:
        stack = []
        for num in nums:
            node = TreeNode(num)  # 숫자를 트리로 변환
            while stack and stack[-1].val < num:  # 현재 숫자가 stack중 젤 큰 동안
                node.left = stack.pop()  # stack에 있는애들 전부 left로
            if stack:
                stack[-1].right = node
            stack.append(node)
        return stack[0]
