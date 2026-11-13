class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # 내일이 더 비싸? 오늘: 삼ㅇㅇ 팔ㄴㄴ
        # 내일이 더 싸? 오늘: 삼ㄴㄴ 팔ㅇㅇ
        account = -1  # 가격이 0원인 경우도 있어서 초기값 -1로
        profit = 0
        for i in range(len(prices)-1):
            todayPrice = prices[i]
            if todayPrice < prices[i+1]:
                if account == -1:
                    account = todayPrice
            elif todayPrice > prices[i+1]:
                if account != -1:
                    todayProfit = todayPrice - account
                    profit += todayProfit
                    account = -1
        # 제일 마지막날 주식 가지고 있으면 팔기
        if account != -1:
            profit += prices[-1] - account
        return profit
