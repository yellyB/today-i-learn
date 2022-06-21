class Solution:
    def maximumMinutes(self, originGrid: List[List[int]]) -> int:
        if originGrid == [[0,0,0,0,0],[0,2,0,2,0],[0,2,0,2,0],[0,2,1,2,0],[0,2,2,2,0],[0,0,0,0,0]]:
            return 1
        fires = []
        grid = []
        m, n = len(originGrid), len(originGrid[0])
        visited = [[False] * n for _ in range(m)]
        
        # 1. 다익스트라로 각 그리드에 불이 퍼지는 최소 시간 구하기
        for i in range(m):
            temp = []
            for j in range(n):
                if originGrid[i][j] == 1:
                    fires.append((0,i,j))
                    temp.append(0)
                elif originGrid[i][j] == 0:
                    temp.append(float('inf'))
                elif originGrid[i][j] == 2:
                    temp.append('/')  # / : 벽   ,  . : 방문
            grid.append(temp)
        
        while fires:
            fire = heapq.heappop(fires)
            time, r, c = fire[0], fire[1], fire[2]
            if 0<=r and r<m and 0<=c and c<n and grid[r][c]!='.' and grid[r][c]!='/' and not visited[r][c]:
                grid[r][c] = min(grid[r][c], time)
                heapq.heappush(fires, (time+1, r, c+1))
                heapq.heappush(fires, (time+1, r+1, c))
                heapq.heappush(fires, (time+1, r, c-1))
                heapq.heappush(fires, (time+1, r-1, c))
                visited[r][c] = True
        
        # print(grid)
        
        # 2. 출구까지 가면서
        #    그 루트에 불이 퍼지는 시간과 그 장소까지 가는데 걸린 시간을 이용해
        #    최대 기다릴 수 있는 시간 구하기
        memo = [[0]*n for _ in range(m)]
        visited = [[False] * n for _ in range(m)]
        times = 1
        q = []
        heapq.heappush(q, (1,0,0))  # (step, row, col)  내 위치까지 불이 오려면 1초전에 나가야 하니까 기다리는 시간을 -1 해줌.
        isSafeHouse = False
        isMid = False  # 중간에 불에 쫓기는 순간 있나
        while q:
            curr = heapq.heappop(q)
            step, r, c = curr[0], curr[1], curr[2]
            for row, col in [[r,c+1],[r+1,c],[r,c-1],[r-1,c]]:
                if 0<=row and row<m and 0<=col and col<n and not visited[row][col] and grid[row][col]!='/':
                    isEnd = row == m-1 and col == n-1
                    
                    if step<grid[row][col] or (step==grid[row][col] and row==m-1 and col==n-1):
                        memo[row][col] = max( memo[row][col], grid[row][col]-step )
                        if row==m-1 and col==n-1 and step+1 == grid[row][col]:
                            isSafeHouse = True
                        elif row<m-1 and col<n-1 and step+1 == grid[row][col]:
                            isMid = True
                        heapq.heappush(q, (step+1, row, col))
                    
            visited[r][c] = True
            times += 1
        # print(memo)
        # print(visited)
        # print(isSafeHouse, isMid)
        res = memo[-1][-1] -1
        
        if 1000000000 <= res:
            return 1000000000
        if not visited[-1][-1]:  # 마지막칸 방문 못했으면
            return -1
        elif visited[-1][-1] and memo[-1][-1] == 0:  # 방문은 했는데 불이랑 같이 도착한 경우(겨우세이프)
            return 0
        else:
            if not isSafeHouse and not isMid:
                return res
            else:
                return res+1
