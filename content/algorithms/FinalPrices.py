class Solution:
    def finalPrices(self, prices: List[int]) -> List[int]:
        for i in range(len(prices) - 1):
            for price in prices[i + 1:]:
                if prices[i] >= price:
                    prices[i] -= price
                    break
        return prices

    # 걍 이중포문 돌림