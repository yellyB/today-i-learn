class Solution:
    def nearestExit(self, maze: List[List[str]], entrance: List[int]) -> int:
        # 다익스트라
        n,m = len(maze), len(maze[0])
        visited = [[False] * m for _ in range(n)]
        location = [(0, entrance[0], entrance[1])]  # 좌표랑 몇칸이동했나 저장
        
        while location:
            curr = heapq.heappop(location)
            row, col = curr[1], curr[2]
            
            if 0<=row<n and 0<=col<m:
                if visited[row][col] or maze[row][col] == '+': continue
                    
                for r, c in [[-1,0], [0,-1], [0,1],[1,0]]:
                    heapq.heappush(location, (curr[0]+1, row+r, col+c) )
                visited[row][col] = True
            else:
                if curr[0] != 1:  # 출구 찾았는데 거기가 시작위치인 경우는 1이 저장돼있음. 이건 제외
                    return curr[0]-1
                
        return -1  # 아예 불가능
