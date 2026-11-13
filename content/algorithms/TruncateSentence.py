class Solution:
    def truncateSentence(self, s: str, k: int) -> str:
        answer = ''
        for a in s:
            if a==' ':
                k-=1
                if k==0:
                    break
            answer+=a
        return answer