class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        rows = []
        for row in range(rowIndex+1):
            tempRow = []
            for i in range(0, row):
                if i == 0:
                    tempRow.append(1)  # 0번째에 1붙임
                else:
                    tempRow.append(rows[row-1][i-1] + rows[row-1][i])
            tempRow.append(1)  # 마지막에 1붙임
            rows.append(tempRow)
        return rows[rowIndex]