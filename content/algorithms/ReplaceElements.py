class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        if len(arr) == 1: return [-1]

        maxNum = -1
        for i in range(len(arr) - 1, -1, -1):
            arr[i], maxNum = maxNum, max(maxNum, arr[i])

        return arr

    # 뒤부터 돌면서 현재max와 지금 값을 비교해 max를 갱신한다.