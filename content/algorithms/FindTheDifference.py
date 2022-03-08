class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        # 아스키 코드 이용
        ascS = 0
        ascT = ord(t[-1])
        for i in range(len(s)):
            ascS += ord(s[i])
            ascT += ord(t[i])
        return chr(ascT - ascS)
