class Solution:
    def groupThePeople(self, groupSizes: List[int]) -> List[List[int]]:
        # 1. 딕셔너리에 들어가야 하는 개수를 키로 인덱스를 모으고
        gCnt = {}  # group count
        for i,gs in enumerate(groupSizes):
            if gs in gCnt:
                gCnt[gs].append(i)
            else:
                gCnt[gs] = [i]
        
        # 2. key를 가지고 배열을 잘라줌
        answer = []
        for key, values in gCnt.items():
            for v in range(0, len(values), key):
                answer.append(values[v:v+key])
        
        return answer
