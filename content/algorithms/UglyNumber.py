class Solution:
    def isUgly(self, n: int) -> bool:
        def isUgly(n):
            if n == 0:
                return False
            if n == 1:
                return True
            result = False
            for num in [2, 3, 5]:
                if n % num == 0:
                    return isUgly(n / num)
            return False

        return isUgly(n)