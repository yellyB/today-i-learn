class Solution:
    def sumOddLengthSubarrays(self, arr: List[int]) -> int:
        # 0번부터 반복문.
        # 홀수개씩 부분배열 만들어서 합계에더했음
        length = len(arr)
        total = 0

        for i in range(length):
            for j in range(i + 1, length + 1, 2):
                sub = arr[i:j]
                total += sum(sub)

        return total