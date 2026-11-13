class Solution:
    def spiralMatrixIII(self, rows: int, cols: int, rStart: int, cStart: int) -> List[List[int]]:
        res = []
        targetCnt = rows * cols  # 추가해야할 개수
        diff = 2  # 가야하는 방향으로 이동해야하는 칸 수 (1,1,2,2,3,3,4,4...식으로 증가함)
        dx, dy = 0, 1  # 방향 전환용 변수. (0,1) (1,0) (0,-1) (-1,0) 순으로 방향 전환
        while targetCnt > 0:
            for _ in range(diff // 2):
                if 0<=rStart<rows and 0<=cStart<cols:  # matrix 내부일 경우만 추가
                    res.append([rStart, cStart])
                    targetCnt -= 1  # 추가해야할 남은 개수는 감소
                rStart += dx  # 다음 인덱스를 위해 가야할 칸 수 만큼 증or감
                cStart += dy
            dx, dy = dy, -dx  # 방향 전환
            diff += 1  # diff를 하나씩 올려줘서 %2했을 때 2개 증가할때마다 1씩 증가하도록
        return res
    
    # 방향전환과 몇칸을 가야할지 규칙을 찾는게 중요
    
    
