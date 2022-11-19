# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pseudoPalindromicPaths (self, root: Optional[TreeNode]) -> int:
        # 컨셉: set 으로 val 개수의 홀,짝 을 관리해서 팰린드롬 판단
        def dfs(root, cnts):
            if not root:
                return 0
            
            if root.val in cnts:
                cnts.remove(root.val)
            else:
                cnts.add(root.val)
                
            # not root 일때 아래처럼 리턴하면 ex2같은 경우 depth3의 1번 노드 다음꺼가 left, right 둘 다 카운팅 됨
            if not root.left and not root.right:
                return 1 if len(cnts) <= 1 else 0  # 개수가 홀수인 애 한개까진 팰린드롬 되니까
            
            return dfs(root.left, set(cnts)) + dfs(root.right, set(cnts))  # set copy 해서 넘겨줌
        
        return dfs(root, set())