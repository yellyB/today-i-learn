class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        answer = []
        for row in range(numRows):
            tempRow = []
            for i in range(0, row):
                if i == 0:
                    tempRow.append(1)  # 0번째에 1붙임
                else:
                    tempRow.append(answer[row-1][i-1] + answer[row-1][i])
            tempRow.append(1)  # 마지막에 1붙임
            answer.append(tempRow)
        return answer