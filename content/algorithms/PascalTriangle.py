class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        rows = [[1] * (i + 1) for i in range(numRows)]  # 하나씩 늘어나면서 1로 들어가게 초기화해줌
        for i in range(2, len(rows)):
            for j in range(1, i):
                rows[i][j] = rows[i - 1][j - 1] + rows[i - 1][j]
        return rows

    # 아니 풀었었는데 왜 풀었다고 체크 안됨? ㅡㅡ
    # 개선해서 다시 풂