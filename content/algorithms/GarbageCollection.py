class Solution:
    def garbageCollection(self, garbage: List[str], travel: List[int]) -> int:
        def calculate(garbageType, value):
            truck[garbageType][0] += value + truck[garbageType][1]
            truck[garbageType][1] = 0  # 다음번에 또 쓰레기가 있으면 그땐 현재 위치부터 다음 쓰레기가 있는 위치까지의 거리만 계산해줘야 해서, 초기화해줌
            return
            
        travel.insert(0, 0)  # garbage랑 인덱스 맞추려고 첫칸에 추가
        truck = {'G':[0, 0], 'P':[0, 0], 'M':[0, 0]}  # 각 트럭별 [쓰레기점수, 걸린시간]
        for i, g in enumerate(garbage):
            for truckType in ['G', 'P', 'M']:
                truck[truckType][1] += travel[i]
            paper, glass, metal = g.count('P'), g.count('G'), g.count('M')
            if paper:
                calculate('P', paper)
            if glass:
                calculate('G', glass)
            if metal:
                calculate('M', metal)
            
        res = 0
        for v in truck.values():
            res += v[0]
        return res