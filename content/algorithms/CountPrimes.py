class Solution:
    def countPrimes(self, n: int) -> int:
        prime = [True] * n  # 일단 소수로 간주하고 전부 true저장
        if n <= 1:
            return 0
        primeCnt = 0  # 소수 갯수
        sqrt = math.sqrt(n)
        i = 2
        while i < sqrt:
            if prime[i] == True:
                j = i + i
                while j < n:
                    prime[j] = False
                    j += i
            i += 1
        return prime.count(True) - 2  # 0과 1은 카운트에서 빼줌