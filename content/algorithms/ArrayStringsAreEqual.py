class Solution:
    def arrayStringsAreEqual(self, word1: List[str], word2: List[str]) -> bool:
        one=''
        two=''
        for w in word1:
            one+=w
        for w in word2:
            two+=w
        return one==two