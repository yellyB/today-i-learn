class Solution:
    def maxIncreaseKeepingSkyline(self, grid: List[List[int]]) -> int:
        cnt = 0
        maxRow = [max(i) for i in grid]  # row중 최고값
        maxCol = [max(j) for j in zip(*grid)]  # col중 최고값

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                nowHeight = grid[i][j]
                highest = min(maxRow[i], maxCol[j])
                cnt += highest - nowHeight

        return cnt