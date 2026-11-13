class Solution:
    def isPalindrome(self, x: int) -> bool:
        string = str (x)
        length=len(string)
        for i in range(length//2):
            if string[i]!=string [length-1-i]:
                return False
        return True