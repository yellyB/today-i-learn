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
                node.left = stack.pop()  # stack에 있는애들(모아둔애들) 전부 left로
            if stack:
                # stack에 값이 있다는건 일단 현재 num이 최고값은 아니란얘기
                # 그리고 stack에 값이 이미 있다는건 stack의 -1이 나보다는 크다는 뜻.(내가 더 컸다면 위 while에서 걸렸을테니)
                # 그러니 right에 붙여줌
                stack[-1].right = node
            stack.append(node)
        return stack[0]
