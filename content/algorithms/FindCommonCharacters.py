class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        first = words[0]  # 기준이 될 단어
        answer = []
        for s in first:
            inAllStr = True  # 기준 단어의 각 글자가 나머지 단어들에 포함되어있는지
            for i, word in enumerate(words[1:]):
                if s not in word:
                    inAllStr = False
                    break
                else:
                    words[i+1] = word.replace(s,'',1)  # word에서 s를 한개만 바꾸겠다
            if inAllStr:
                answer.append(s)
        return answer