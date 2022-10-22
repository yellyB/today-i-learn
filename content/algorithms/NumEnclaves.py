class Solution:
    def numEnclaves(self, grid: List[List[int]]) -> int:
        def walk(i, j):
            if i<0 or j<0 or i>=m or j>=n:
                return
            if grid[i][j] == 0:
                return
            grid[i][j] = 0
            walk(i, j+1)
            walk(i+1, j)
            walk(i, j-1)
            walk(i-1, j)
            return
        
        m, n = len(grid), len(grid[0])
        for i in range(m):
            for j in range(n):
                if (i == 0 or j == 0 or i == m-1 or j == n-1 ) and grid[i][j] == 1:
                    walk(i, j)
                    
        cnt = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    cnt += 1
                    
        
        return cnt