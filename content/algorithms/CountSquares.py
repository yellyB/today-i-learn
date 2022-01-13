class Solution:
    def countSquares(self, matrix: List[List[int]]) -> int:
        cnt = 0
        rowLen = len(matrix)
        colLen = len(matrix[0])
        memo = [[0] * (colLen + 1) for _ in range(rowLen + 1)]

        for i in range(rowLen):
            for j in range(colLen):
                if matrix[i][j] == 1:  # 내가 1이면? 일단 적어도 1개짜리 사각형임
                    memo[i][j] = min(memo[i - 1][j], memo[i - 1][j - 1], memo[i][j - 1]) + 1
                    cnt += memo[i][j]
        return cnt

    # 원래 matrix보다 한칸씩 넓은 기록용 배열 만들음
    # side2인 정사각형 = 나=1이고 대각위, 위, 왼 이 다 1이어야함
    # side3인 정사각형 = 나=1이고 대각위, 위, 왼이 다 2여야함
    # ...

    # https://leetcode.com/problems/maximal-square/
    # 221. Maximal Square
    # 위 문제랑 비슷. 아니 거의 같은문제..