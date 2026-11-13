class Solution:
    def updateBoard(self, board: List[List[str]], click: List[int]) -> List[List[str]]:
        '''
        [case1. 지뢰 클릭]
        클릭한 곳 X로 변경하고 끝
        
        [case2. 지뢰 외 클릭]
        다음다음칸이 지뢰면
        지뢰 만나면 주변에 1씩 추가해야 되는데
        '''
        def dfs(board, i, j):
            if board[i][j] != 'E':  # 이미 체크한 칸이면 E가 아닐거임
                return
            
            m, n = len(board), len(board[0])
            directions = [(-1,0), (-1,1), (0,1), (1,1), (1,0), (1,-1), (0,-1), (-1,-1)]
            mine_cnt = 0
            
            for d in directions:
                next_i, next_j = i+d[0], j+d[1]
                if 0 <= next_i < m and 0 <= next_j < n and board[next_i][next_j] == 'M':  # 다음칸이 지뢰면 숫자 올리고 멈춰야 함
                    mine_cnt += 1
            
            if mine_cnt > 0:
                board[i][j] = str(mine_cnt)  # 다음칸이 지뢰면 지뢰 몇갠지 기록하고 스탑
                return
            
            board[i][j] = 'B'  # 지뢰 없으면 빈칸으로 칸 오픈
            
            for d in directions:
                next_i, next_j = i+d[0], j+d[1]
                if 0 <= next_i < m and 0 <= next_j < n:
                    dfs(board, next_i, next_j)
        
        
        
        if board[click[0]][click[1]] == 'M':
            board[click[0]][click[1]] = 'X'
            return board  # 지뢰 클릭시 얼리리턴
        else:
            dfs(board, click[0], click[1])
            return board
        