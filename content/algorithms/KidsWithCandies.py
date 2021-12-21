class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        maxValue = max(candies)
        answer = []
        for cnt in candies:
            if cnt + extraCandies < maxValue:
                answer.append(False)
            else:
                answer.append(True)
        return answer