class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        cnt = 0
        checked = []
        
        
        def dfs(conn):
            for i in range(len(conn)):
                if i not in checked and conn[i] == 1:
                    checked.append(i)
                    dfs(isConnected[i])
            return
        
        for i in range(len(isConnected)):
            if i not in checked:
                cnt += 1
                checked.append(i)
                dfs(isConnected[i])
        
        return cnt
    
    
