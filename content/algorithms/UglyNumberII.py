class Solution:
    def nthUglyNumber(self, n: int) -> int:
        fac2, fac3, fac5 = 0, 0, 0
        uglyNums = [1]
        while n > 1:
            lastNum = uglyNums[-1]
            n2 = uglyNums[fac2] * 2
            n3 = uglyNums[fac3] * 3
            n5 = uglyNums[fac5] * 5
            newNum = min(n2, n3, n5)

            if n2 == newNum:
                fac2 += 1
            if n3 == newNum:
                fac3 += 1
            if n5 == newNum:
                fac5 += 1

            uglyNums.append(newNum)
            n -= 1
        return uglyNums[-1]

# 인수에 2, 3, 5만 가지고 있어야 하니까
# 2, 3, 5의 곱 조합으로 만들 수 있는 숫자이면 uglyNumber임
# 2가 몇개, 3이 몇개, 5가 몇개인지 갯수를 저장하고 (fac2, fac3, fac5)
# 각 갯수의 곱 중에 가장 작은 애를 다음 순서 uglyNum으로 저장한다.
