class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        colLen = len(matrix[0])
        for i in range(1, len(matrix)):
            for j in range(colLen):
                matrix[i][j] = min(matrix[i - 1][max(0, j - 1)], matrix[i - 1][j],
                                   matrix[i - 1][min(colLen - 1, j + 1)]) + matrix[i][j]
        return min(matrix[-1])

    # 윗줄 3개랑 자기자신 더한값을 계속 갱신 저장함
    # 마지막줄 min값