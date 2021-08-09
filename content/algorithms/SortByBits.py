class Solution:
    def sortByBits(self, arr: List[int]) -> List[int]:
        cntList = []
        answer= []
        def getNumberOfOne(num):  # 어떤 십진수 n이 이진수일때 1 갯수 반환
            # 2로 나눠서 나머지가 1이다? 이진수에서 1개수 증가시킴됨
            cnt = 0
            while num > 0:
                cnt += num % 2
                num = num//2  # 몫을 그 다음 피제수로
            return cnt

        arr.sort()  # 일단 한 번 정렬
        for n in arr:
            cntList.append([n,getNumberOfOne(n)])
        cntList.sort(key=lambda x: x[1])

        for cnt in cntList:
            answer.append(cnt[0])
        return answer