class Solution:
    def minInsertions(self, s: str) -> int:
        n = len(s)
        dp = [ [0]*(n+1) for i in range(n+1) ]
        for i in range(1, n+1):
            for j in range(1, n+1):
                if s[n-i] == s[j-1]:
                    dp[i][j] = dp[i-1][j-1] + 1  # 같을 때 표시하고 나중에 값 반전
                else:
                    dp[i][j] = max(dp[i-1][j-1], dp[i-1][j], dp[i][j-1])
        # print(dp)
        return n - dp[-1][-1]
    
    # edit distance 응용
    # 문자열과 거꾸로한 문자열을 순서대로 비교했을 때
    # 띄엄띄엄이라도 공통된 가장 긴 문자열 있으면 걔네 빼고 추가해주면 되기 때문에
    # 사실상 LCA랑 비슷.
    # 그래서 공통된 것 기록하고 나중에 len 에서 빼주는것
