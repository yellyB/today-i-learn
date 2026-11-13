class Solution:
    def matrixReshape(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:
        # 행,열 안맞으면 원래꺼 리턴
        if len(mat) * len(mat[0]) != r * c: return mat

        numList = [val for row in mat for val in row]  # 값만 뽑아
        newMat = [[0] * c for _ in range(r)]
        idx = 0
        for i in range(r):
            for j in range(c):
                newMat[i][j] = numList[idx]
                idx += 1
        return newMat