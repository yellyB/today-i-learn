class Solution:
    def maximum69Number (self, num: int) -> int:
        typeStr = str(num)
        return typeStr.replace('6','9',1)