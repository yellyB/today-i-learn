class Solution:
    def countBattleships(self, board: List[List[str]]) -> int:
        cnt = 0
        for i in range (len (board)):
            for j in range (len(board [0])):
                if board [i][j]=='X':
                    # 시작점 한개만 체크할거임
                    if i>0 and board [i-1][j]=='X': continue
                    if j>0 and board [i][j-1]=='X': continue
                    cnt += 1
        return cnt