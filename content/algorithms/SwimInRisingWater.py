class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        n = len(grid)
        memo = [[float('inf')] * n for _ in range(n)]  # 처음엔 inf 값으로 초기화
        visited = [[False] * n for _ in range(n)]
        stack = [(0,0,0)]  # (0,0)=현재위치랑 이전값
        dirs = [[-1,0], [0,-1], [0,1],[1,0]]
        
        while stack:
            # val = stack.pop()
            val = heapq.heappop(stack)
            row, col = val[1], val[2]
            if 0<=row<n and 0<=col<n and visited[row][col]==False:
                for r, c in dirs:
                    # (이전값, 현grid) 중 max를, 메모돼있는(처음엔 inf값인) 값과 비교해서 min값을 메모함
                    memo[row][col] = min(memo[row][col], max(grid[row][col], val[0]))
                    # stack.append((row+r,col+c,memo[row][col]))  # 다음 검사할 위치와 이전값이 될 현재 메모값
                    heapq.heappush(stack, (memo[row][col],row+r,col+c) )
                    # print(stack)
                visited[row][col] = True
            # if row==0and col==1:
                # break
        print(memo)
        
        
        return memo[-1][-1]
    
    # 다익스트라
    # https://namu.wiki/w/%EB%8B%A4%EC%9D%B5%EC%8A%A4%ED%8A%B8%EB%9D%BC%20%EC%95%8C%EA%B3%A0%EB%A6%AC%EC%A6%98
