class Solution:
    def countServers(self, grid: List[List[int]]) -> int:
        cnt = 0
        m, n = len(grid), len(grid[0])
        rows = [0] * m
        cols = [0] * n

        for i in range(m):
            for j in range(n):
                if grid[i][j]:
                    rows[i] += 1
                    cols[j] += 1

        for i in range(m):
            for j in range(n):
                if grid[i][j] and (rows[i] >= 2 or cols[j] >= 2):
                    # 가로 세로 중 한개라도 2개이상 연결된게 있다면(붙어있지 않아도 됨)
                    # 현재 컴터는 어딘가와는 연결된 애
                    cnt += 1

        return cnt
