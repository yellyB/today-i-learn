class Solution:
    def snakesAndLadders(self, board: List[List[int]]) -> int:
        # 칸 번호 받아서 좌표를 리턴해주는 함수
        def getCoordinate(pos):
            r, c = divmod(pos-1, n)  # 좌표별 라벨이 1베이스라서 인덱스 구하기 위해 pos에서 1뺌
            c = (n-1)-c if r%2==1 else c  # 몫이 짝수인 경우와 홀수인 경우 col이 어디서 시작하는지 달라서 따로 처리
            r = (n-1)-r
            return r, c
        
        n = len(board)
        q = [1]
        visited = set()
        step = 0
        
        while q:
            temp = []
            for curr in q:
                row, col = getCoordinate(curr)
                if board[row][col] != -1:  # 있는곳이 뱀이나 사다리라면?
                    curr = board[row][col]  # 해당위치로 이동
                if curr == n*n: return step  # 끝에 다다르면 리턴
                for i in range(1, 7):
                    nexts = curr + i
                    if nexts <= n*n and nexts not in visited:
                        temp.append(nexts)
                        visited.add(nexts)
            step += 1
            q = temp[:]
        
        return -1
