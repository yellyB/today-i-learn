class Solution:
    def minSetSize(self, arr: List[int]) -> int:
        freq = collections.defaultdict(int)
        targetLen = len(arr) // 2
        # 1. 숫자별 빈도수
        for a in arr:
            freq[a] += 1

        # 2. 빈도수 높은거부터 제거해야 유리하니까 밸류 내림차순정렬
        sortVals = sorted(freq.values(), reverse=True)  # 밸류 기준 desc
        removeCnt = 0
        # 3. 제거한 카운트 증가시키면서 목표숫자넘었다? 그럼 그 인덱스만큼의 갯수를 제거한거임
        for i in range(len(sortVals)):
            removeCnt += sortVals[i]
            if removeCnt >= targetLen:
                break
        return i + 1