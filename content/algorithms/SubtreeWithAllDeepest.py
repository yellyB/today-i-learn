# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def subtreeWithAllDeepest(self, root: TreeNode) -> TreeNode:
        def dfs(root, depth):
            if not root: return root, depth-1
            
            leftRes = dfs(root.left, depth+1)
            rightRes = dfs(root.right, depth+1)
            
            if leftRes[1] > rightRes[1]:
                return leftRes
            elif leftRes[1] < rightRes[1]:
                return rightRes
            else:
                return root, leftRes[1]  # left랑 right 둘 다 같은 depth니까 걍 leftDepth로 리턴
        
        
        res = dfs(root, 0)
        return res[0]
    
    # 예시1번 같은 경우 왜 2,7,4를 선택하냐면 7,4가 가장 깊기 때문.
    # 얘네는 뎁스 3인데 그럼 그 윗노드인 2는 옆에애인 6과 비교했을 때 더 깊은 자식을 가지고있음
    # 그럼 노드 2는 최고뎁스 3인거고 6은 2인거. 그럼 노드 2를 선택해야함
    # 그러니까 재귀 안에서는 최고뎁스랑 최고뎁스인 서브 루트를 리턴해야겠군
    # 노드의 left,right을 비교해서 더 큰 쪽은 선택해야하고 같으면 자기자신 리턴하면됨
