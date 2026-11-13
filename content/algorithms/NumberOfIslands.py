class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        rowLen = len(grid)
        colLen = len(grid[0])
        cnt = 0

        def isLand(i, j):
            if 0 > i or i >= rowLen or 0 > j or j >= colLen:
                return
            if grid[i][j] == "1":
                grid[i][j] = 1

                isLand(i - 1, j)
                isLand(i, j - 1)
                isLand(i + 1, j)
                isLand(i, j + 1)

        for i in range(rowLen):
            for j in range(colLen):
                if grid[i][j] == "1":
                    isLand(i, j)
                    cnt += 1

        return cnt