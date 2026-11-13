# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        answer = []
        stack = [root]
        while True:
            tempAnswer = []
            tempStack = []
            while stack:
                node = stack.pop(0)
                if not node: break
                tempAnswer.append(node.val)
                if node.left:
                    tempStack.append(node.left)
                if node.right:
                    tempStack.append(node.right)
            if not tempAnswer: return answer
            answer.append(tempAnswer)
            stack = tempStack

    # answer와 stack을 만들고 반복문 안에서 그 두개의 각temp를 또 만듦
    # 한 level이 끝날때마다(stack이 없으면 현 level탐색 끝난것으로 간주)
    # 모아놓은 tempAnswer를 찐 답에 붙임
    # 두 temp는 초기화되고! 계속 반복