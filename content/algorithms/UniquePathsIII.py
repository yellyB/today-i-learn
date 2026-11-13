class Solution:
    def uniquePathsIII(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        empty = 1  # 밟아줘야 하는 칸 개수(시작위치때문에 1로 초기화)
        start = []  # 시작 위치 저장
        for row in range(m):
            for col in range(n):
                if grid[row][col] == 0:
                    empty += 1
                if grid[row][col] == 1:
                    start.append(row)
                    start.append(col)
                    
        def dfs(row, col, pathCnt):
            # grid 범위 벗어나면 실패
            if not 0<=row<m or not 0<=col<n:
                return 0
            # 벽에 막힘 or 이미 밟음
            if grid[row][col] == -1 or grid[row][col] == 3:
                return 0
            
            # 목적지 도착
            if grid[row][col] == 2:
                if pathCnt == empty:  # 모든 곳 밟았다면
                    return 1
                else:
                    return 0
            
            grid[row][col] = 3  # 밟은곳 표시
            
            res = 0
            res += dfs(row, col+1, pathCnt+1)
            res += dfs(row+1, col, pathCnt+1)
            res += dfs(row, col-1, pathCnt+1)
            res += dfs(row-1, col, pathCnt+1)
            
            # 이 dfs오기전의 dfs와 동일한 depth 중
            # 다른 방향으로 가는 dfs를 위해서 밟은 칸을 원래대로 되돌려줌
            grid[row][col] = 0
            
            return res
        
        return dfs(start[0], start[1], 0)
