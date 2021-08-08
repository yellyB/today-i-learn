class Solution:
    def frequencySort(self, str: str) -> str:
        sList = list(str)
        sDict = {}
        answer = ''

        sList.sort()  # 일단 한 번 정렬
        for s in sList:
            if s in sDict:
                sDict[s] += 1
            else:
                sDict[s] = 1

        sort = sorted(sDict, key=lambda x: sDict[x], reverse=True)  # 밸류 기준 desc

        for s in sort:
            cnt = sDict[s]
            answer += s * cnt

        return answer