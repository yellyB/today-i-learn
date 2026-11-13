class Solution:
    def replaceWords(self, dictionary: List[str], sentence: str) -> str:

        # 하나씩 늘려가며 그게 딕셔너리에 있나. 무식하게 검사
        def replaceWord(word):
            for i in range(len(word)):
                if word[:i] in dictionary: return word[:i]
            return word

        answer = ''
        for word in sentence.split(' '):  # 공백으로 스플릿해갖구 그 리스트를 돌림
            answer += replaceWord(word) + ' '

        return answer[:-1]  # 마지막에 공백 붙으니까 걔 빼고