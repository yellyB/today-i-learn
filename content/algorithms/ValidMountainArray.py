class Solution:
    def validMountainArray(self, arr: List[int]) -> bool:
        maxNum = max(arr)
        maxNumIdx = arr.index(maxNum)
        if maxNumIdx == 0 or maxNumIdx == len(arr)-1 :
            return False
        for i in range(0,maxNumIdx):
            if arr[i] >= arr[i+1]:
                return False
        for i in range(maxNumIdx, len(arr)-1):
            if arr[i] <= arr[i+1]:
                return False
        return True