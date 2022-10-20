# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findFrequentTreeSum(self, root: Optional[TreeNode]) -> List[int]:
        # 문제: 가장 빈도수 많은 subtree 합계
        res = collections.defaultdict(int)
        
        def getSum(root, sums):
            if not root:
                return 0
            
            nowSum = getSum(root.left, sums)+getSum(root.right, sums)+root.val  # 왼+오+자신
            res[nowSum] += 1
            
            return nowSum

        getSum(root, 0)
        
        
        
        maxVal = max(res.values())
        return [s for s in res if res[s] == maxVal]
