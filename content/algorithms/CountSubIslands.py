class Solution:
    def countSubIslands(self, grid1: List[List[int]], grid2: List[List[int]]) -> int:
        m, n = len(grid2), len(grid2[0])
        cnt = 0
        
        def bfs(i, j):
            if 0<=i<m and 0<=j<n and grid2[i][j] == 1:
                grid2[i][j] = 0
                
                
                return grid1[i][j] & bfs(i, j+1) & bfs(i+1, j) & bfs(i, j-1) & bfs(i-1, j)
                
                # 이 방법으로 하면 왜 안되지 ㅜㅜ (and -> & / if 문 분기처리도 하면 통과 안됨)
                # ex1 에서 (4,3)이 같이 카운트 됨
                # if grid1[i][j] == 1:
                #     return bfs(i, j+1) and bfs(i+1, j) and bfs(i, j-1) and bfs(i-1, j)
                # else:  # 그리드1이 섬 아니면 얜 불가
                #     return 0
                
            else:  # 범위 벗어날때까지 버텼으면 얜 서브 섬이나 마찬가지
                return 1
        
        
        '''
        1. 그리드2 값이 1이면?
        2. 그리드1을 체크. 얘도 1이어야함
        3. 그리고 거기랑 연결된 그리드2를 계속 체크 & 그리드1도 똑같이 1인지 계속계속 체크
           (그리드2가 더이상 1이 아니면 카운트 하나 올리고 리턴하고, 그리드1이 1이 아니면 서브섬이 아닌 셈. 얘는 카운트 ㄴㄴ)
        '''
        for i in range(m):
            for j in range(n):
                if grid2[i][j] == 1:
                    cnt += bfs(i, j)
                    
        return cnt
