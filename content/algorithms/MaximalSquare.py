class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        rowLen = len(matrix)
        colLen = len(matrix[0])
        maxCnt = 0
        grid = [[0] * (colLen + 1) for i in range(rowLen + 1)]

        for i in range(rowLen):
            for j in range(colLen):
                if matrix[i][j] == "1":  # 내가 1이면 대각아래에 아래,나, 오른을 확인함. (무조건 1 이상이 저장되는데 여기서의 1은 사각형이 자기자신 1개란뜻)
                    grid[i + 1][j + 1] = min(grid[i + 1][j], grid[i][j], grid[i][j + 1]) + 1
                    maxCnt = max(maxCnt, grid[i + 1][j + 1])

        return maxCnt * maxCnt