import numpy as np

class Solution:
    def numSquares(self, n: int) -> int:
        dp =  [0] * (n+1)
        dp[1] = 1
        for i in range(2, n+1):
            mins = float('inf')
            # 어떤 수를 제곱한 수가 num범위 안이려면
            # num의 제곱근을 버림해서 나온 수까지 검사해야함(=num보다 작은 제곱수찾기)
            for j in range(1, int(np.sqrt(i))+1):
                rest = i - j*j
                mins = min(mins, dp[rest])
            dp[i] = mins + 1  # for문에서 j*j로 perfect square를 하나 계산한 상태기때문에 1 더해줌
        # print(dp)
        return dp[n]
        
