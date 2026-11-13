class Solution:
    def earliestFullBloom(self, plantTime: List[int], growTime: List[int]) -> int:
        pair = []
        bloomDay = 0
        plantDay = 0
        for i in range(len(plantTime)):
            pair.append([plantTime[i], growTime[i]])
        
        # grow가 오래걸리는 씨앗을 먼저 심어야
        # 얘가 grow하는 동안 다른애들이 plant할수있음. 그래서 grow기준 역순 정렬
        pair.sort(key = lambda x:x[1], reverse=True)

        for p in pair:
            plantDay += p[0]
            bloomDay = max(bloomDay, plantDay+p[1])  # plant와 grow날짜 합쳐서 bloom구함
        
        return bloomDay
