class Solution:
    def slidingPuzzle(self, board: List[List[int]]) -> int:
        # 12345만 들어옴
        moves = {0:(1,3), 1:{0,2,4}, 2:(1,5), 3:(0,4), 4:(1,3,5), 5:(2,4)}  # 그렇기 때문에 움직일 수 있는 위치 한정되어있음
        state = ''.join(str(c) for c in board[0]+board[1])  # 현재 상태
        startIdx = state.index('0')  # 0에서 시작하기 위해 0의 인덱스 알아냄
        visited = set()
        
        q = collections.deque([(startIdx, state, 0)])
        while q:
            currIdx, state, steps = q.popleft()
            if state == '123450':
                return steps
            elif state in visited:
                continue
            else:
                visited.add(state)
                for nextIdx in moves[currIdx]:
                    stateList = list(state)
                    stateList[currIdx], stateList[nextIdx] = stateList[nextIdx], stateList[currIdx]  # 자리 이동
                    stateStr = ''.join(stateList)
                    q.append((nextIdx, stateStr, steps+1))
        
        return -1  # 움직일 수 있는 가능성 다 체크했는데 없으면 실패