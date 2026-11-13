class Solution:
    def deleteGreatestValue(self, grid: List[List[int]]) -> int:
        res = 0
        for row in range(len(grid)):
            grid[row] = sorted(grid[row])

        for j in range(len(grid[0])):
            temp = []
            for i in range(len(grid)):
                temp.append(grid[i][j])
            res += max(temp)

        return res
