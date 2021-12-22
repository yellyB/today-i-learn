# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if not root: return False
        if not root.left and not root.right:  # 이 node가 끝이면
            if root.val == targetSum: return True
        targetSum -= root.val
        return self.hasPathSum(root.left, targetSum) or self.hasPathSum(root.right, targetSum)

# 이 밑에꺼 제대로 짠 거 같은데 왜 안되는지 의문
# example 1 돌릴때 파란색 루트대로 11까지 더한 상태에서
# 내가 따로 분기처리해서 2를 실행해보면 True가 잘 나옴.
# 근데 return a or b 하는 부분에서 뭔가 잘못되었는지
# 11에서 7과 2를 실행해 그 결과를 리턴하면 False가 나옴.. or 이니까 하나는 True잖아 ㅠ 왜False나오는데ㅅㅂ
#         def calcSum(root, sums):
#             if not root:
#                 if sums == targetSum: return True  # 1
#                 else: return False
#             if sums + root.val >= targetSum: return False  # 2
#             return calcSum(root.left, sums+root.val) or calcSum(root.right, sums+root.val)

#         return calcSum(root, 0)

#     # 1: 끝까지 가는동안 중단되지 않았으니 성공했단뜻
#     # 2: 왜 타겟과 같아도 실패냐? "1에서 실패하지 않=끝노드아님"인데 벌써 타겟이랑 같음 안됨