class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        totalLandCnt = [0]  # 각 섬의 땅 갯수들
        width = len(grid[0])
        height = len(grid)
        visited = [[False] * width for i in range(height)]

        def checkIsLand(i, j):
            cnt = 0
            if grid[i][j] == 1 and not visited[i][j]:
                visited[i][j] = True
                cnt += 1
                if i > 0:
                    up = checkIsLand(i - 1, j)
                    cnt += up
                if j > 0:
                    left = checkIsLand(i, j - 1)
                    cnt += left
                if i + 1 < height:
                    under = checkIsLand(i + 1, j)
                    cnt += under
                if j + 1 < width:
                    right = checkIsLand(i, j + 1)
                    cnt += right

                return cnt
            return cnt

        for i in range(height):
            for j in range(width):
                if grid[i][j] == 1:
                    if not visited[i][j]:
                        result = checkIsLand(i, j)
                        totalLandCnt.append(result)  # 재귀로 얻은 땅의 갯수 저장

        return max(totalLandCnt)

# 맨 왼쪽 위의 땅을 시작점으로 거기의 네 면을 재귀로 확인
# 방문한 적 있으면 pass
# 처음 방문이면 카운트 +1 하고  다 확인했으면 최종 땅 면적에 저장