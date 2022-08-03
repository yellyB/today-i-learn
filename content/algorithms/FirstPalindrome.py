class Solution:
    def firstPalindrome(self, words: List[str]) -> str:
        def isPal(word):
            s, e = 0, len(word)-1
            while s < e:
                if word[s] == word[e]:
                    s += 1
                    e -= 1
                else:
                    return False
            return True
        
        for word in words:
            if isPal(word):
                return word
        
        return ''
