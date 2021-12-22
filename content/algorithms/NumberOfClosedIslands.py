class Solution:
    def closedIsland(self, grid: List[List[int]]) -> int:
        rowLen = len(grid)
        colLen = len(grid[0])
        cnt = 0

        def isLand(i, j):
            if 0 > i or i >= rowLen or 0 > j or j >= colLen: return False

            if grid[i][j] == -2:
                return False
            if grid[i][j] == -1:
                return True
            if grid[i][j] == 0:
                if 0 == i or i == rowLen - 1 or 0 == j or j == colLen - 1: return False
                grid[i][j] = -1

                if not isLand(i - 1, j):
                    grid[i][j] = -2
                    return False
                if not isLand(i, j - 1):
                    grid[i][j] = -2
                    return False
                if not isLand(i + 1, j):
                    grid[i][j] = -2
                    return False
                if not isLand(i, j + 1):
                    grid[i][j] = -2
                    return False
            return True

        for i in range(1, rowLen - 1):
            for j in range(1, colLen - 1):
                if grid[i][j] == 0:
                    if isLand(i, j):
                        grid[i][j] = -1
                        cnt += 1

        return cnt

    # 일단 붙어있는 0의 갯수를 셈
    # 세면서 0이 가생이에 있는 경우면 갯수세기 취소
    # 유효한 섬으로 확인됨 : -1   유효하지않은 섬으로 확인됨 : -2