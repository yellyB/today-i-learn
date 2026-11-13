class Solution:
    def medianSlidingWindow(self, nums: List[int], k: int) -> List[float]:
        res = []
        even = k % 2 == 0
        mid = k // 2
        if even:  # 짝수면 두개를 뽑아야 하기 때문
            mid -= 1
        for i in range(len(nums)):
            if i+1 >= k:
                lis = nums[i-k+1:i+1]
                lis.sort()
                if even:
                    res.append(sum(lis[mid:mid+2])/2)
                else:
                    res.append(lis[mid])
        return res
