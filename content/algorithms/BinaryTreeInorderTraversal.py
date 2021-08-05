# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        def getInorder(root):
            inorder = []

            if root.left:
                inorder.extend(getInorder(root.left))  # left가 있으면 추가
            inorder.extend([root.val])  # 두번째 순서인 val추가(val은 무조건 있으니)
            if root.right:
                inorder.extend(getInorder(root.right))  # right도 있다면 추가
            return inorder

        if not root:
            return []

        return getInorder(root)