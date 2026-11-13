class Solution:
    def maxConsecutiveAnswers(self, key: str, k: int) -> int:
        cnts = collections.Counter()
        maxCnt = 0
        l = 0

        for r in range(len(key)):
            cnts[key[r]] += 1

            while k < cnts['T'] and k < cnts['F']:  # T, F 중 하나가 k를 벗어나는건 용납ㅇㅇ
                cnts[key[l]] -= 1
                l += 1
                
            maxCnt = max(maxCnt, r-l+1)

        return maxCnt
