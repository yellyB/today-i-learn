class Solution:
    def minimumAbsDifference(self, arr: List[int]) -> List[List[int]]:
        arr.sort()
        minDiff = abs(arr[0] - arr[1])
        answer = []
        for i in range(len(arr) - 1):
            diff = abs(arr[i] - arr[i + 1])
            if minDiff == diff:
                answer.append([arr[i], arr[i + 1]])
            elif minDiff > diff:
                minDiff = diff
                answer = [[arr[i], arr[i + 1]]]
            elif minDiff < diff:
                pass
        return answer
