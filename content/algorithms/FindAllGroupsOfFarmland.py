class Solution:
    def findFarmland(self, land: List[List[int]]) -> List[List[int]]:
        rowLen = len(land)
        colLen = len(land[0])
        answer = []

        def checkBottom(i, j):
            if i < rowLen and land[i][j] == 1:
                return checkBottom(i + 1, j)
            else:
                return i - 1

        def checkRight(i, j):
            if j < colLen and land[i][j] == 1:
                return checkRight(i, j + 1)
            else:
                return j - 1  # 둘 다 해당 안되면 이 함수로 보내기 전 j까지만 1이란 뜻

        for i in range(rowLen):
            for j in range(colLen):
                if land[i][j] == 1:
                    if (i - 1 < 0 or land[i - 1][j] == 0) and (j - 1 < 0 or land[i][j - 1] == 0):
                        bottom = checkBottom(i + 1, j)
                        right = checkRight(i, j + 1)
                        # print('right:',right)
                        # print('bottom:',bottom)
                        answer.append([i, j, bottom, right])
        return answer

    # 어차피 farmLand는 사각형으로 이루어져 있어서  ( [1,1][1,0] 같은거 불가 )
    # 현재 위치가 1이면 오른쪽과 아래쪽을 확인(함수로빼서) -> 다음칸이 0이거나 끝이면 그 위치를 반환해줌
    # 아래쪽의 끝은 farmland의 끝row, 오른쪽의 끝은 끝col이 될거임