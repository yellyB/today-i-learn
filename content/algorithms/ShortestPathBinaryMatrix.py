class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        n = len(grid)
        q = deque([(0,0,0)])  # 맨 처음 값. (i, j, 0개수)
        
        # 첫 칸이 1이면 절대 불가
        if grid[0][0] == 1: return -1
        
        while q:
            x, y, d = q.popleft()
            
            # 끝을 찾았으면 종료해줌
            if x == n-1 and y == n-1: return d+1
            
            for dx, dy in ((1, 0), (1, 1), (0, 1), (-1, 1),
                           (-1, 0), (-1, -1), (0, -1), (1, -1)):
                newX, newY = dx + x, dy + y
                
                if 0 <= newX < n and 0 <= newY < n and grid[newX][newY] == 0:
                    grid[newX][newY] = 1  # visit
                    q.append((newX, newY, d + 1))
        return -1
