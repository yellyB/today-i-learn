class Solution:
    def restoreMatrix(self, rowSum: List[int], colSum: List[int]) -> List[List[int]]:
        # 그 칸의 행,열 비교해서 젤 작은 합계를 고르고 남은 행열에서 그 값만큼 빼줌
        m, n = len(rowSum), len(colSum)
        res = [[0]*n for _ in range(m)]
        for i in range(m):
            for j in range(n):
                res[i][j] = min(rowSum[i], colSum[j])
                rowSum[i] -= res[i][j]
                colSum[j] -= res[i][j]
        return res