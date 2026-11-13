class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        # 1. 맨위,맨왼 -> 1이면 갈수 있는 방법 없으므로 0을 저장.
        #                 + 이전께 돌이어서 0저장되었다면 뒤에도 못가니까 0 저장

        rowLen = len(obstacleGrid)
        colLen = len(obstacleGrid[0])

        obstacleGrid[0][0] = 1 if obstacleGrid[0][0] != 1 else 0
        for i in range(1, rowLen):
            if obstacleGrid[i][0] != 1 and obstacleGrid[i - 1][0] != 0:
                obstacleGrid[i][0] = 1
            else:
                obstacleGrid[i][0] = 0
        for j in range(1, colLen):
            if obstacleGrid[0][j] != 1 and obstacleGrid[0][j - 1] != 0:
                obstacleGrid[0][j] = 1
            else:
                obstacleGrid[0][j] = 0

        # 2. 나머지 부분 돌면서 현재위치가 1(돌)이 아니라면 위랑왼쪽 경우의 수를 더해줌
        for i in range(1, rowLen):
            for j in range(1, colLen):
                if obstacleGrid[i][j] == 1:
                    obstacleGrid[i][j] = 0
                else:
                    obstacleGrid[i][j] = obstacleGrid[i - 1][j] + obstacleGrid[i][j - 1]

        return obstacleGrid[-1][-1]

