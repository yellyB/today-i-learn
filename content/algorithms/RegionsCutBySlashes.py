class Solution:
    def regionsBySlashes(self, grid: List[str]) -> int:
        rowLen = len(grid)
        colLen = len(grid[0])
        regionCnt = 0
        # 한 칸을 3x3으로 나눠서 각 칸에 True 저장
        region = [([True] * 3) * rowLen for i in range(colLen * 3)]

        def doMark(row, col, n):  # n: col위치에 계속 +n할거임
            for i in range(3):
                region[row][col] = False
                col += n
                row += 1
            return

        # 1. 3x3으로 나눈걸 슬래시 정,역 에따라 True->False로 바꿈
        for i in range(rowLen):
            for j in range(colLen):
                if grid[i][j] == '/':
                    doMark(i * 3, (j * 3) + 2, -1)  # 시작 위치 전달
                elif grid[i][j] == '\\':
                    doMark(i * 3, j * 3, 1)

        # print(region)

        # 사방확인. 연결된 True칸을 False로(중복 카운트 방지)
        def checkLegion(row, col):
            region[row][col] = False
            if region[row][max(0, col - 1)]: checkLegion(row, max(0, col - 1))  # 왼
            if region[min(len(region) - 1, row + 1)][col]: checkLegion(min(len(region) - 1, row + 1), col)  # 밑
            if region[row][min(len(region[0]) - 1, col + 1)]: checkLegion(row, min(len(region[0]) - 1, col + 1))  # 오
            if region[max(0, row - 1)][col]: checkLegion(max(0, row - 1), col)  # 위
            return

        # 2. True로만 묶인 구역 갯수 세기
        for i in range(rowLen * 3):
            for j in range(colLen * 3):
                if region[i][j]:
                    regionCnt += 1
                    checkLegion(i, j)

        return regionCnt