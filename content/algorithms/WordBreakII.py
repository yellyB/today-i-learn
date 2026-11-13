class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        def isInDict(start, words):
            # 4. 3에서 end+1하기 땜에 시작위치가 len(s)라면 정상적으로 찾은거
            if start == len(s):
                answer.append(' '.join(words))
            # 2. 넘겨받은 시작위치 ~ 끝위치 하나씩 알파벳 추가해서 검사
            for end in range(start, len(s)):
                word = s[start:end+1]
                # 3-1. 사전에 있으면 (시작위치는+1, 찾은 목록에 추가)해서 다음 재귀로 넘김
                if word in wordDict:
                    res = isInDict(end+1, words+[word])
                    # print(word, res)
                # 3-2. 없으면 다음꺼 계속
                else: continue
            return []

        answer = []
        # 1. 재귀 함수로 (시작위치, 사전에 있는 목록) 넘김
        isInDict(0, [])

        return answer