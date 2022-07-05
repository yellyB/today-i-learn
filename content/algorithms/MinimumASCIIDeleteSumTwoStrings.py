class Solution:
    def minimumDeleteSum(self, s1: str, s2: str) -> int:
        # edit distance 알고리즘
        m, n = len(s1), len(s2)
        dp = [[0] * (m+1) for _ in range(n+1)]
        
        for i in range(len(s1)):
            dp[0][i+1] = dp[0][i] + ord(s1[i])
        
        for i in range(len(s2)):
            dp[i+1][0] = dp[i][0] + ord(s2[i])
        
        
        for i in range(1, n+1):
            for j in range(1, m+1):
                if s1[j-1] == s2[i-1]:
                    dp[i][j] = dp[i-1][j-1]
                else:
                    # 이전 세 경우를 어느 문자를 없애는게 나은지 비교
                    dp[i][j] = min(dp[i][j-1] + ord(s1[j-1]), dp[i-1][j] + ord(s2[i-1]), dp[i-1][j-1] + ord(s1[j-1]) + ord(s2[i-1]))
        # print(dp)
        
        return dp[-1][-1]


#         @lru_cache(None)
#         def dp(s1, s2, sums):
#             # case 1: 둘 다 빈문자열
#             if s1 == '' and s2 == '':
#                 return sums
#             # case 2: 둘 중 하나 빈문자열 -> 아직 남아있는 문자열을 sums에 전부 더한다.
#             if s1 == '':
#                 return dp(s1, s2[1:], sums+ord(s2[0]))
#             if s2 == '':
#                 return dp(s1[1:], s2, sums+ord(s1[0]))
            
#             asc1 = ord(s1[0])
#             asc2 = ord(s2[0])
            
#             # case 3: 둘다 첫글자 동일
#             if asc1 == asc2:
#                 return dp(s1[1:], s2[1:], sums)
            
#             # 그 외에는 두 문자열을 하나씩 뺀걸 비교해서 리턴
#             return min( dp(s1[1:], s2, sums+asc1), dp(s1, s2[1:], sums+asc2)  )
        
        
#         return dp(s1, s2, 0)
    
    
    

