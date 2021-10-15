class Solution:
    def calPoints(self, ops: List[str]) -> int:
        answer = []

        def add(num1, num2):
            return num1 + num2

        def double(num):
            return 2 * num

        for o in ops:
            if o == '+':
                answer.append(add(answer[-1], answer[-2]))
            elif o == 'C':
                answer.pop()
            elif o == 'D':
                answer.append(double(answer[-1]))
            else:
                answer.append(int(o))

        return sum(answer)