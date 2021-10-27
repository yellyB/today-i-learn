class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        buy, buy1 = -prices[0], -prices[0]
        sell, sell1 = 0, 0
        for i in range(len(prices)):
            todayPrice = prices[i]
            buy = max(buy1, sell1 - todayPrice)  # 어제 산, 어제 판 + 오늘가격
            sell = max(sell1, todayPrice + buy1 - fee)  # 어제 판, 오늘가격 - 어제 산 - 요금
            buy1, sell1 = buy, sell
        return sell

    # 팔 때 fee 계산하는 것으로
    # 어제 - 오늘 비교해서 계산
    # buy : 어제의 buy, 어제 sell 하고난거에 오늘가격 buy
    # sell :  어제의 sell, 어제 buy 하고난거에 오늘가격으로 sell
