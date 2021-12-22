class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        orinLen = len(nums)
        nums = set(nums)
        return orinLen != len(nums)

    # 원래 len과 중복 제거후의 len 비교. 중복되는게 있다면 다르겠찌?