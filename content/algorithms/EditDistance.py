class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        m, n = len(word1), len(word2)
        dp = [list(range(n+1))]+[[i+1]+[0]*n for i in range(m)]  # [[0, 1, 2, 3], [1, 0, 0, 0], [2, 0, 0, 0], ...] 형태로
        
        for i in range(1, m+1):
            for j in range(1, n+1):
                if word1[i-1] == word2[j-1]:
                    dp[i][j] = dp[i-1][j-1]
                else:
                    dp[i][j] = min(dp[i][j-1], dp[i-1][j], dp[i-1][j-1]) + 1

        return dp[-1][-1]
        
        
        # 이중배열로 두 문자열을 x축 y축으로 구성한다음 각 알파벳끼리 같은지 다른지 비교
        # dp에 기록되는 숫자는 알파벳이 달라서 바꿔줘야 하는 횟수 기록(누적값)
        
        # 알파벳이 다를경우 word1이나 word2중 어떤걸 delete하거나 혹은 하나를 다른 문자열에 맞춰 replace할수있음
        # 현재dp[i][j]의 왼쪽위에 있는 3가지 칸들은
        # 이전에 delete나 replace했을때의 가장적게 변형하는 결과가 저장되어 있음
        # 그러니 그 중 가장 적게 변형하는 경우에 +1해주면 됨.
        # 알파벳이 같은 경우는 변형 안해도 되니까 +1안해줌. 그냥 두 문자열의 바로 앞전 알파벳을 검사한 결과를 그대로 가져오면됨
        
        # dp를 맨 첫 row랑 col을 0,1,2,...로 채우는 이유
        #  ㄴ 맨 첫줄들은 각 알파벳이 아니라 공백을 나타냄
        #     공백은 어떤 알파벳과도 다르기 때문에 다름카운트를 계속 증가시키는것
        
        
        
        
        # 풀이는 다르지만 약간 비슷한 문제▼
        # 583. Delete Operation for Two Strings
