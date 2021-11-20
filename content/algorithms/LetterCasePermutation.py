class Solution:
    def letterCasePermutation(self, s: str) -> List[str]:
        answer = [s]
        for i,letter in enumerate(s):
            if letter.isalpha():
                temp = []
                for word in answer:
                    temp.append(word[:i] + word[i].swapcase() + word[i+1:])
                answer.extend(temp)
        return answer