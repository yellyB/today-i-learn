class Solution:
    def maxIceCream(self, costs: List[int], coins: int) -> int:
        costs.sort()
        cnt = 0
        for cost in costs:
            coins -= cost
            if coins < 0:
                return cnt
            cnt += 1

        return cnt