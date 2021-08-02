# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def sumRootToLeaf(self, root: TreeNode) -> int:
        def getSum(root:TreeNode, prev) -> int:
            leftRightSum = 0  # 왼,오 값의 합계를 한꺼번에 윗 노드에 리턴할꺼임
            if not root.left and not root.right:
                return prev + root.val  # 젤 아래 노드 값 = 앞에값 + 현재값
            # 왼,오가 둘다 null이 아니라면
            # 위에값+현재값 을 제곱해서 아래 노드로 전달
            # 왜냐면 아래로 한칸 씩 내려갈수록 2의 제곱수가 하나씩 증가하기 때문
            if root.left:
                leftRightSum += getSum(root.left, (prev+root.val)*2)
            if root.right:
                leftRightSum += getSum(root.right, (prev+root.val)*2)
            return leftRightSum
        return getSum(root, 0)