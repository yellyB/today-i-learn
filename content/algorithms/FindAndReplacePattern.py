class Solution:
    def findAndReplacePattern(self, words: List[str], pattern: str) -> List[str]:
        # 문자를 문자형태숫자로 바꿔서 패턴 저장
        # 맨 처음 등장하면 1번으로 쭉 번호 매겨서 또 나오면 매겼던 번호로 패턴 등록할거임
        def getPattern(word):
            pattern = ''
            for w in word:
                if w in checked:
                    pattern += str(checked.index(w))  # count로 등장횟수 세는게 나을까??
                else:
                    pattern += str(len(checked))
                    checked.append(w)
            return pattern
        pattern = getPattern(pattern)
        answer = []
        for word in words:
            if pattern == getPattern(word):
                answer.append(word)
        return answer