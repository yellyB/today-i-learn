class Solution:
    def countSubstrings(self, s: str) -> int:
        def isPalindromic(word):
            half = len(word) // 2
            for i in range(half):
                if word[i] != word[-i - 1]:
                    return False
            return True

        cnt = 0
        length = len(s)
        for start in range(length):
            for end in range(start + 1, length + 1):
                if isPalindromic(s[start:end]): cnt += 1

        return cnt

    # 그냥 단어 각각 전부 확인해서 팰린드롬이면 +1함...