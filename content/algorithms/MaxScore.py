class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        # 0에서 len-k번째 합을 총합에서 빼고 오른쪽으로 한 칸씩 이동해서 계속 함
        # 빼는 값이 가장 적은게 총합이 가장 클것임
        totalSum = sum(cardPoints)
        length = len(cardPoints)
        startIdx = 0
        endIdx = (length) - k
        initSum = sum(cardPoints[startIdx:endIdx])
        subArrList = [initSum]
        while endIdx < length :
            initSum = initSum + cardPoints[endIdx] - cardPoints[startIdx]
            subArrList.append(initSum)
            startIdx += 1
            endIdx += 1
        return totalSum - min(subArrList)