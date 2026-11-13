class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        # bottom up
        dp = [0] * (amount + 1)
        dp[0] = 1
        for coin in coins:
            for amt in range(coin, amount + 1):
                # 남은 액수에서 동전 거슬러주고 났을때
                # 그 나머지 금액이 과거에 몇개의 조합이 있었는지 찾아봄
                dp[amt] += dp[amt - coin]

        return dp[-1]