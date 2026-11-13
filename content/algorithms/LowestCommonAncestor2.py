# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        def recursion(root):
            if not root: return False
            
            left = recursion(root.left)
            right = recursion(root.right)
            
            # 밑에서 리턴할때 root를 리턴하기때문에(다른건 boolean형태)
            # TreeNode를 리턴했을경우(정답인경우)는 따로 처리해줌
            if type(left) == TreeNode: return left
            if type(right) == TreeNode: return right
            
            mid = root == p or root == q  # 자기 자신이 조상일수도있기때문
            
            if mid + left + right >= 2:  # 세가지 경우중 2개가 true여야함
                return root
            
            return mid or left or right  # 하나라도 True면
            
        return recursion(root)
