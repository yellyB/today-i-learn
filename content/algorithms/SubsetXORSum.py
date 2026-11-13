class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        def func(res, arr):
            if not arr: return res
            res1 = func(res^arr[0], arr[1:])
            res2 = func(res, arr[1:])
            return res1+res2
        
        return func(0, nums)
