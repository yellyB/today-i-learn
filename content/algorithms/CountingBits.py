class Solution:
    def countBits(self, n: int) -> List[int]:
        answer = []

        # 십진수 숫자를 이진수로 바꿨을 때 1의 갯수 구하기
        # => 이진수로 바꾸는 과정을 진행하면서 나머지가 1일때가 있으면 1갯수에 추가
        def getNumberOfOne(num):
            cnt = 0
            while num > 0:
                cnt += 1 if num % 2 == 1 else 0
                num = num // 2
            return cnt

        for i in range(0, n + 1):
            answer.append(getNumberOfOne(i))

        return answer