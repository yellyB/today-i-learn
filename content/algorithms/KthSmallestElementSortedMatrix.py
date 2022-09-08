class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        # 각 배열이 오름차순이라 바이너리 서치 사용 가능
        
        row = col = len(matrix)
        lo, hi = matrix[0][0], matrix[-1][-1]
        
        while lo < hi:
            mid = lo + (hi - lo) // 2  # 중간 값을 구함(인덱스 ㄴㄴ)
            cnt = 0
            
            for r in range(row):
                c = col - 1  # 끝에서부터
                while 0 <= c and matrix[r][c] > mid:  # 중간값 만날때까지 범위를 하나씩 앞으로 땡김
                    c -= 1
                
                if 0 <= c:
                    cnt += (c + 1)  # 인덱스인 c 이용해서 지금 r에서의 mid 보다 작은 개수를 구해 누적. 이 개수가 k 랑 같아지면 그게 정답
                else:
                    break
            
            # mid 보다 작은 개수랑 k랑 비교해봐서 범위 새로 잡기
            if cnt < k:
                lo = mid + 1
            else:
                hi = mid
        
        return lo
