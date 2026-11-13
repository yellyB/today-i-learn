class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # 첫 가격을 최소가격으로 임시 저장
        # 반복문돌면서 지금까지이익, 오늘팔았을때 이익 중 큰 가격 저장
        # 그리고 현재 가격이 임시최소가격보다 작으면 교체
        profit = 0
        tempMinPrice = prices[0]
        for price in prices:
            tempProfit = price - tempMinPrice
            profit = max(profit, tempProfit)
            if price < tempMinPrice:
                tempMinPrice = price
        return profit