# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        result = []
        stack = [root]
        while stack:
            node = stack.pop()
            if node:
                result.append(node.val)
                stack.append(node.right)
                stack.append(node.left)
        return result

    # stack에 전부 집어넣고 하나씩 꺼냄
    # 첨엔 초기값으로 넣은 한개있고 그 한개가 전부일거임
    # 걔의 val이 있다면 결과에 넣고 걔의 왼과 오는 스택에 다시 넣음
    # 근데 꺼낼때 뒤에부터 꺼내니까 나중에 꺼내져야 하는 오른을 먼저 넣음
    # 여기서 값이 null이 (예를들어 오른쪽은null이었음) 들어가면 다음 반복문때 걸러야함
    # 그래서 if node: 를 쓰는거