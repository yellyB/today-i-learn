# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def addOneRow(self, root: Optional[TreeNode], val: int, depth: int) -> Optional[TreeNode]:
        if not root:  # 왼쪽은 있는데 오른쪽은 없는 경우 오른쪽은 빈값 올 수 있음
            return None
        if depth == 1:
            return TreeNode(val, root, None)   # 뎁스1이면 1번째에 값 넣고 리턴
        
        if depth == 2:  # 왼쪽은 왼쪽, 오른은 오른쪽에 위치해야 해서 분기처리
            root.left = TreeNode(val, root.left, None)  # 왼쪽 애들은 val 추가 후 왼쪽으로 붙여주고
            root.right = TreeNode(val, None, root.right)  # 오른쪽 애들은 오른쪽으로 붙여줌
        else:
            root.left = self.addOneRow(root.left, val, depth-1)
            root.right = self.addOneRow(root.right, val, depth-1)
        return root
