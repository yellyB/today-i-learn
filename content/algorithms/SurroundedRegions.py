class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        
        # 외곽에 위치한 0 저장
        safePlace = []
        row, col = len(board), len(board[0])
        for i in range(row):
            if board[i][0] == 'O': safePlace.append((i, 0))
            if board[i][col-1] == 'O': safePlace.append((i, col-1))
        for j in range(col):
            if board[0][j] == 'O': safePlace.append((0, j))
            if board[row-1][j] == 'O': safePlace.append((row-1, j))
        
        # 외곽의 0과 붙어있는애들도 x로 안바뀌도록
        q = safePlace[:]
        neighbours = [(1, 0), (0, 1), (-1, 0), (0, -1)]
        while q:
            i, j = q.pop()
            for a, b in neighbours:
                nx, ny = i+a, j+b
                if 0 <= nx < row and 0 <= ny < col and board[nx][ny] == 'O' and (nx, ny) not in safePlace:
                    q.append((nx, ny))
                    safePlace.append((nx, ny))
        
        # 전체 돌면서 safePlace 에 없는애들 바꿔주기
        for i in range(row):
            for j in range(col):
                if board[i][j] == 'O' and (i, j) not in safePlace:
                    board[i][j] = 'X'
                    
