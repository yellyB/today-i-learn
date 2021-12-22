# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        stack = [root]
        while True:
            currLevel = []  # 현재 레벨의 모든 밸류들 쭉
            tempStack = []
            while stack:
                node = stack.pop(0)
                # 빈 노드일시 비었다는 뜻으로 범위밖값인 101을 넣어줌.
                if not node:
                    currLevel.append(101)
                    continue
                currLevel.append(node.val)
                tempStack.append(node.left if node.left else None)
                tempStack.append(node.right if node.right else None)
            if not currLevel: break
            reverse = currLevel[:]
            reverse.reverse()
            if currLevel != reverse: return False
            stack = tempStack
        return True

    # 102. Binary Tree Level Order Traversal 응용