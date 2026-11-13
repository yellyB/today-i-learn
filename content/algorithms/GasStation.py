class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        
        # if sum(gas) < sum(cost): return -1  # 총 비용이 더 크면 절대불가
        
        minCurr = gas[0]-cost[0]  # 이익이 젤 작은 누적 값 저장
        idx = 0  # 젤 작은 순간의 가스 인덱스 저장
        totalGas = 0  # 현재까지의 가스
        
        for i in range(len(gas)):
            currProfit = gas[i] - cost[i]  # 현재 턴 이득본 가스
            totalGas += currProfit
            if totalGas < minCurr:
                minCurr = totalGas
                idx = i
                
        if totalGas < 0: return -1
        return idx+1 if idx+1<len(gas) else 0
    
    # 비용과 가스 따져서 가장 적게 이득보는 충전소를 찾음.
    # 그곳을 가장 마지막에 들러야함
    
            
        
        
