class Solution:
    def squareIsWhite(self, coordinates: str) -> bool:
        answer = False
        # print(ord(coordinates[0]) - ord('a'))
        # print(ord(coordinates[1]) - ord('1'))
        if (ord(coordinates[0]) - ord('a')) % 2 == 1:
            answer = not answer
        if (ord(coordinates[1]) - ord('1')) % 2 == 1:
            answer = not answer

        return answer

# 하나건너 색 바뀌니까 알파벳이랑 숫자로 분리해서(행, 열) black인 a1을 기준으로 홀인지 짝인지 판별
# = 행 열을 차례로 반전시킴