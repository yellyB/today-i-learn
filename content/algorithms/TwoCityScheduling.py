class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        total = 0
        diff = []  # 도시 A와 도시 B의 가격 차이를 인덱스와 함께 저장
        
        for i, cost in enumerate(costs):
            diff.append([cost[0]-cost[1], i])
        
        sort = sorted(diff, key=lambda x: x[0])  # [0]오름차순 정렬. [0]이 클수록 B로가는 비용이 더 크단뜻
        half = len(costs)//2
        
        # 반 나눠서 앞쪽은 A로, 나머진 B로 가면 됨
        for s in sort[:half]:
            total += costs[s[1]][0]  # diff에서 저장한 인덱스의 A도시비용 더해줌
        for s in sort[half:]:
            total += costs[s[1]][1]
        
        
        return total
