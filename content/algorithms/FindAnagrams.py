class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        answer = []
        if len(s) < len(p): return answer
        pList = [0] * 26
        sList = [0] * 26
        gap = len(p)
        
        # p의 길이만큼 돌려서 샘플 만들고(p) s도 그만큼 이동
        for i in range(gap):
            sList[ord(s[i])-97] += 1
            pList[ord(p[i])-97] += 1
        
        # 이번에는 이동하는만큼 맨 앞 문자는 빼줌
        for i in range(gap, len(s)):
            if pList == sList:
                answer.append(i-gap)
            sList[ord(s[i])-97] += 1
            sList[ord(s[i-gap])-97] -= 1
        
        # 위 for문에서 먼저 비교한다음 증감하기 때문에
        # 마지막에 한번 더 검사해주기
        if pList == sList:
            answer.append(i+1-gap)

        return answer
    
    # sliding window
    # 알파벳 아스키코드 이용
