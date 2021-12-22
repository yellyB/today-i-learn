class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy, buy1 = -prices[0], -prices[0]  # buy -> 맨 처음에는 일단 사야지 뭘 파니까 비용을 먼저 지불하기 때문에 무조건 마이너스다.
        sell, sell1, sell2 = 0, 0, 0  # sell1 -> i-1번째 판거 / sell2 -> i-2번째 판거
        for i in range(len(prices)):
            todayPrice = prices[i]
            buy = max(sell2 - todayPrice, buy1)  # 이틀전에 팔고난 잔고에 오늘 가격을 뺌 (샀으니까 빼주는거)
            sell = max(buy1 + todayPrice, sell1)  # 어제 샀던 경우에 오늘가격 더하면 = 내잔고
            # 밑에는 이제 하루씩 밀어주기 (오늘은 어제로 바꾸고 어제는 그제로 바꿈)
            buy1 = buy
            sell1, sell2 = sell, sell1
        return sell


# buy랑 sell에는 내 잔고 상태를 저장할거임
# sell은 팔고난 오늘의 내 잔고, sell1은 어제의 팔고난 내 잔고, sell2는 그저께 팔고난 잔고임, buy도 마찬가지

# return : 잔고가 0인 상태로 끝나야 이득이 최대이기 때문에(사느라 돈 냈으면 팔아야지) 맨 마지막에는 sell을 리턴할거임

# i일때
# 사는 경우 : [i-2에서 팔고 i에서 사는경우] [i-1에 저장된 i-1에 사는경우의 최대값을 저장한것]  => 두가지 비교
# 파는 경우 : [i-1에서 산걸 파는경우] [i-1에 저장된 i-1에 파는경우의 최대값] => 두개 비교

# 사는 경우는 cooldown때문에 i-1에 팔고 i에 사는경우를 보는게 아님. i에서 사려면 최소 i-2에서 팔았어야 함

