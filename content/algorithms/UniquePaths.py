class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        grid = [[1] * n for i in range(m)]
        for i in range(1, m):
            for j in range(1, n):
                grid[i][j] = grid[i - 1][j] + grid[i][j - 1]
        # print(grid)
        return grid[-1][-1]

    # 걍 누적 구하면 그게 경우의 수
    # 위랑 왼쪽 각 첫줄은 경우의수가 모두 1임
    # (1,1)은 2가지, (1,2)는 앞에 그 두가지에 위쪽에서 오는거 +1해서 3개.
