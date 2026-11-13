class Solution:
    def divisorSubstrings(self, num: int, k: int) -> int:
        cnt = 0
        numToStr = str(num)
        for i in range(0, len(numToStr)-k+1):
            sliced = int(numToStr[i:i+k])
            if sliced != 0 and num % sliced == 0:
                cnt += 1

        return cnt
