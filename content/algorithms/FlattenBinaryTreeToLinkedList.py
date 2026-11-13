# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        '''
        [컨셉]
        노드가 붙는 순서가, val->left->right기 때문에
        현재 트리에서 right는 현재 트리 모든 left를 확인한 뒤에 그제서야 붙을거임.
        그러니까 right 는 left의 가장 마지막 우측에 붙이자
        '''
        while root:
            if root.left:
                currLeft = root.left
                # 1. 현재 트리 left의 가장 우측 찾기
                while currLeft.right:
                    currLeft = currLeft.right
                currLeft.right = root.right  # 2. 가장 우측 찾았으면 거기에 현재트리 right 붙이기

                root.right = root.left  # 3.  2번까지 작업한 left를 right에 붙여주기
                root.left = None  # 4. left 를 오른쪽에 붙여줬으니 left 는 비워줌
            root = root.right  # 5. 모든거 right에 붙였으니 다음 right 를 탐색 ㄱㄱ
