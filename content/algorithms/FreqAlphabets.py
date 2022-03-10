class Solution:
    def freqAlphabets(self, s: str) -> str:
        for i in range(26, 0, -1):
            toReplace = str(i) + '#' * (i>9)
            s = s.replace(toReplace, chr(96+i))
        return s
    
    # 26부터 거꾸로 돌면서 i가 9보다 클때만 i에 #을 붙임
    # 그 문자를 알파벳으로 바꾸기
