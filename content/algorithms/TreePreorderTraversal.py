"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def preorder(self, root: 'Node') -> List[int]:
        if not root: return []
        
        stack = [root]
        answer = []
        while stack:
            node = stack.pop()
            answer.append(node.val)  # 현 노드 정답에 추가
            for child in node.children[::-1]:  # 자식들을 먼저 들어간애가 나중에 나오니까 거꾸로 스택에쌓음
                stack.append(child)
        return answer
