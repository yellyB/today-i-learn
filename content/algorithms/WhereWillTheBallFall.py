class Solution:
    def findBall(self, grid: List[List[int]]) -> List[int]:
        def dfs(i, j):
            if i<0 or j<0:
                return -1
            if i>=m or j>=n:
                return j
            
            if grid[i][j] == 1:
                if j+1 < n and grid[i][j+1] == 1:
                    return dfs(i+1, j+1)
                else:
                    return -1
            else:
                if j-1 >= 0 and grid[i][j-1] == -1:
                    return dfs(i+1, j-1)
                else:
                    return -1
            return
        
        m, n = len(grid), len(grid[0])
        res = []
        for x in range(n):
            res.append(dfs(0, x))
        return res