class Solution:
    def numBusesToDestination(self, routes: List[List[int]], source: int, target: int) -> int:
        # 1. 버스별로 지나가는 정류장 저장
        linked = {}
        for i, route in enumerate(routes):
            for r in route:
                if r in linked: linked[r].append(i)
                else: linked[r] = [i]
        
        
        location = [(0, source)]  # 몇번째탔는지, 버스정류장
        visited = set([source])
        
        while location:
            curr = heapq.heappop(location)
            if curr[1] == target: return curr[0]
            
            # 2. 정류장에 지나는 버스들 확인해서 다음번 검사 목록에 추가
            for bus in linked[curr[1]]:
                for busStop in routes[bus]:
                    if busStop in visited: continue
                    heapq.heappush(location, (curr[0]+1, busStop))
                    visited.add(busStop)
            routes[bus] = []
            
        return -1
