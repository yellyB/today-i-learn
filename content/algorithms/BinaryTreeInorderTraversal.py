# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        stack, result = [], []
        node = root
        while node or stack:
            while node:  # 왼쪽으로 먼저 탐색하며 서브노드를 계속 누적
                stack.append(node)
                node = node.left
            node = stack.pop()
            result.append(node.val)
            node = node.right  # 오른쪽 값. fullnode면 젤 첨에는 null일거임
        return result

    # 중위 순회(Inorder)은 다음의 순서로 진행된다.
    # 왼쪽 서브 트리를 중위 순회한다.
    # 노드를 방문한다.
    # 오른쪽 서브 트리를 중위 순회한다.