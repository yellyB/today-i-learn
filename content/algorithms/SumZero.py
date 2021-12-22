class Solution:
    def sumZero(self, n: int) -> List[int]:
        arr = []
        for i in range(1, n // 2 + 1):
            arr.append(i)
            arr.append(-i)
        if n % 2 != 0:
            arr.append(0)
        return arr

    # n을 반으로 나눠서 반복문 돌림
    # i의 양수값과 음수값을 각각 추가함
    # 만약 n이 홀수라면 마지막에 0 추가함