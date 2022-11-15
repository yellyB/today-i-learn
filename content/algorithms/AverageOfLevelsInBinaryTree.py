# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        res = []
        q = [root]
        temp_q = []
        sums, cnt = 0, 0
        
        while q:
            while q:
                node = q.pop()
                if not node: continue

                sums += node.val
                cnt += 1

                temp_q.append(node.left)
                temp_q.append(node.right)

            if sums != 0:  # division error 방지
                res.append(sums/cnt)
            else:
                if cnt != 0:  # 숫자는 더했지만 합계가 0이라 위에서 패쓰되는 애들 위해
                    res.append(sums/cnt)
                
            q = temp_q[:]
            
            # 초기화
            temp_q = []
            sums, cnt = 0, 0
            
        
        return res