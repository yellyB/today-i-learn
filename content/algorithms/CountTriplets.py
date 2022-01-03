class Solution:
    def countTriplets(self, arr: List[int]) -> int:
        cnt = 0
        for i in range(len(arr)):
            xor = arr[i]
            for j in range(i+1, len(arr)):
                xor ^= arr[j]
                if xor == 0:
                    cnt += j-i
        return cnt