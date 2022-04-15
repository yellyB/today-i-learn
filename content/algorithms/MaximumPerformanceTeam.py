class Solution:
    def maxPerformance(self, n: int, speed: List[int], efficiency: List[int], k: int) -> int:
        worker = []
        for i in range(n):
            worker.append([speed[i], efficiency[i]])
        worker.sort(key=lambda x:x[1], reverse=True)
        print(worker)
        
        queue = []  # speed 작은애부터 저장할
        maxVal = -pow(10, 5)  # sp X eff 해서 최고값. 일단 젤 작은값으로 초기화
        totalSpeed = 0
        for sp, eff in worker:
            if len(queue) < k:  # 아직 k만큼 안모였으면 추가
                heappush(queue, sp)
                totalSpeed += sp
            else:
                if sp > queue[0]:  # eff가 계속 줄어들기때문에 적어도 speed라도 큐에있는애보단 커야 비교할이유가있음
                    totalSpeed -= heappop(queue)
                    heappush(queue, sp)
                    totalSpeed += sp
                
            maxVal = max(maxVal, totalSpeed * eff)
            
        return maxVal %(pow(10, 9) + 7)
    
    """
    efficiency로 내림차순 정렬하고 걔 돌면서 체크
    efficiency랑 짝지어진 speed가 큐에 저장된 애보다 작다면 어차피 바꿀 필요 없음. eff도 작고 speed도 작으니깐
    그렇지않다면 새로운애를 큐에 추가하고 speed가 작은 원래애는 제거해서 계속 계산했던 값이랑 비교
    """
