class Solution:
    def divisorGame(self, n: int) -> bool:
        result = [False] #헷갈리지않게 리스트를 1~n까지 구성하려고 0번째는 아무데이터나 넣음
        result.append(False)  # n이 1이면 짐
        for i in range(2, n+1):
            result.append(False) #n의 약수가 있는지, 있다면 그 수를 냈을때 내가 질지 모르기때문에 일단 false
            for j in range(i-1, 0, -1): #x의 약수중에 가장 큰 수를 냈을때 이길 확률 높기때문에 큰수부터 거꾸로
                if i%j == 0: #약수 검사
                    if result[i-j] == False: #n-x한 새로운 n이 다음사람을 이기게 만들어주는지?
                        result[i] = True
                        break

        return result[n]