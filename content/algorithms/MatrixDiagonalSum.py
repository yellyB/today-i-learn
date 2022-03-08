class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        sums = 0
        rowLen = len(mat)
        rowMid = rowLen // 2

        # i번째,  len-i번째 숫자들 전부 더함
        for i in range(rowLen):
            sums += mat[i][i]
            sums += mat[i][rowLen-1-i]
            # print(mat[i][i], mat[i][rowLen-1-i])
            
        # 가운데 하나 겹치는 경우 = 길이 홀수인 경우
        if rowLen % 2 == 1:
            print(mat[rowMid][rowMid])
            sums -= mat[rowMid][rowMid]
            
        return sums
