class Solution:
    def isHappy(self, n: int) -> bool:
        def getNextNum(n):
            sum = 0
            while n:
                sum += (n % 10) * (n % 10)  # 일의자리부터 일단 제곱 계산
                n //= 10  # 십의자리를 일의자리로 밀어서 또 계산ㄱ
            return sum

        slow, fast = n, getNextNum(n)
        while slow != fast:
            slow = getNextNum(slow)
            fast = getNextNum(getNextNum(fast))

        return slow == 1

    # https://leetcode.com/problems/linked-list-cycle/
    # 141. Linked List Cycle
    # 이 문제랑 비슷
    # two pointer 이용