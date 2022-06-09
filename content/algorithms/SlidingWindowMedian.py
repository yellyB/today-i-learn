class Solution:
    def medianSlidingWindow(self, nums: List[int], k: int) -> List[float]:
        q = []
        medians = []
        for i in range(len(nums)):
            q.append(nums[i])
            if k-1<=i:
                q.sort()
                medians.append(sum(q[1:-1])/(k-2))
                q.remove(nums[i-(k-1)])
        return medians
