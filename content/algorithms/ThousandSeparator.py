class Solution:
    def thousandSeparator(self, n: int) -> str:
        n = str(n)
        leng = len(n)
        if leng <= 3:
            return n
        i = 1
        while i < leng:
            if i % 3 == 0:
                n = n[:leng-i]+'.'+n[leng-i:]
            i = i + 1
        return ''.join(n)