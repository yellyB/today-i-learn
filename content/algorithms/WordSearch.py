class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        for i in range(len(board)):
            for j in range(len(board[0])):
                if self.checkWord(i, j, word, board):
                    return True
        return False

    def checkWord(self, i, j, word, board):
        if len(word) == 0: return True  # word가 다 없어질때까지 False를 안만났으면 True!
        if i < 0 or j < 0 or i > len(board) - 1 or j > len(board[0]) - 1: return False  # 범위 넘어가면 나가리

        if board[i][j] == word[0]:
            board[i][j] = '#'  # 방문으로 바꿈

            # result에 하나라도 True면 True반환할거
            if self.checkWord(i + 1, j, word[1:], board) \
                    or self.checkWord(i, j + 1, word[1:], board) \
                    or self.checkWord(i - 1, j, word[1:], board) \
                    or self.checkWord(i, j - 1, word[1:], board):
                return True

            board[i][j] = word[0]  # 얘를 수정한 상태 그대로 있으면 원본 값이 유지가 안되어서(sibal) 다시 되돌려줌

        return False