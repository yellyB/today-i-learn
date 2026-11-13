class Solution:
    def numTeams(self, rating: List[int]) -> int:
        cnt = 0
        n = len(rating)
        up = [0] * n
        down = [0] * n
        
        
        # 이중포문 돌면서 나보다 앞에있는 애들 중 작/큰 애들 개수를 저장해나감
        # 그 개수가 2개 이상이 된 순간 3명 모집 가능.
        # 근데 이 개수가 1씩 증가할때마다 경우의 수 이기때문에 여러 조합 가능해짐. 누적해야함
        for i in range(n):
            for j in range(i):
                if rating[i] > rating[j]:
                    up[i] += 1  # [i] 보다 앞이면서 작은 개수 카운팅
                    cnt += up[j]  # 현재 잡고있는 애에다가 더해줌. 이렇게하면 2이상일때 자연스럽게 증가됨
                else:
                    down[i] += 1
                    cnt += down[j]
        
        return cnt
