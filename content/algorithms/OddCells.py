class Solution:
    def oddCells(self, m: int, n: int, indices: List[List[int]]) -> int:
        matrix = [[False] * n for i in range(m)]
        cnt = 0
        for idx in indices:
            for i in range(n):
                matrix[idx[0]][i] = not matrix[idx[0]][i]
            for j in range(m):
                matrix[j][idx[1]] = not matrix[j][idx[1]]
        for row in matrix:
            for col in row:
                if col: cnt += 1
        return cnt