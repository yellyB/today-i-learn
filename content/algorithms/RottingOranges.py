class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        # grid를 전부 돌면서 썩.오 있으면 걔의 사방을 다 썩힘.
        #   ㄴ 썩힐때 2로 저장하지 말고 몇 분에 썩은지 알기 위해 minute+2로 저장할거(중복방지)
        # 해당 턴에 썩힌 갯수 0이면 중단
        # 마지막에 grid 다시 돌면서 1인거(싱싱한) 없나 확인

        rowLen = len(grid)
        colLen = len(grid[0])
        minute = 0

        def rotting(i, j):
            cnt = 0  # 하나라도 썩힌게 있나 체크 위해
            if grid[max(0, i - 1)][j] == 1:
                grid[i - 1][j] = 2 + minute + 1
                cnt += 1
            if grid[min(rowLen - 1, i + 1)][j] == 1:
                grid[i + 1][j] = 2 + minute + 1
                cnt += 1
            if grid[i][max(0, j - 1)] == 1:
                grid[i][j - 1] = 2 + minute + 1
                cnt += 1
            if grid[i][min(colLen - 1, j + 1)] == 1:
                grid[i][j + 1] = 2 + minute + 1
                cnt += 1

            return cnt

        while True:
            totalCnt = 0  # 이번턴에 썩힌게 있나 체크 위해
            for i in range(rowLen):
                for j in range(colLen):
                    if grid[i][j] == 2 + minute:  # 이번턴에 썩힌건 체크하지 않기 위해 minute 더함
                        res = rotting(i, j)
                        totalCnt += res
                        grid[i][j] = 3
            if totalCnt == 0:  # 썩힌거 하나도 없었으면 바로 종료
                break
            minute += 1

        # 남아있는 싱싱오렌지 있는지
        for i in range(rowLen):
            for j in range(colLen):
                if grid[i][j] == 1:
                    return -1

        return minute