class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        sum = 0
        for i in range(1, len(grid)):
            grid[i][0] = grid[i - 1][0] + grid[i][0]
        for j in range(1, len(grid[0])):
            grid[0][j] = grid[0][j - 1] + grid[0][j]

        for i in range(1, len(grid)):
            for j in range(1, len(grid[0])):
                grid[i][j] = min(grid[i - 1][j], grid[i][j - 1]) + grid[i][j]

        return grid[-1][-1]

    # 맨 위, 맨 왼은 걍 누적합계 구함
    # 나머지는 위랑 왼 중 작은거 선택
    # 맨 아래,오른 선택하면 끝