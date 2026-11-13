class Solution:
    def reverseWords(self, s: str) -> str:
        def reverse(str):
            str = list(str)
            l, r = 0, len(str) - 1
            while l < r:
                str[l], str[r] = str[r], str[l]
                l += 1
                r -= 1
            return ''.join(str)

        s = s.split(' ')
        answer = []
        for word in s:
            answer.append(reverse(word))
        return ' '.join(answer)