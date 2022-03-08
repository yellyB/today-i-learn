class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        newWord = ''
        len1 = len(word1)
        len2 = len(word2)
        p1 = 0
        p2 = 0
        
        while p1<len1 or p2<len2:
            if p1<len1:
                newWord += word1[p1]
                p1+=1
            if p2<len2:
                newWord += word2[p2]
                p2+=1
        
        return newWord
    
