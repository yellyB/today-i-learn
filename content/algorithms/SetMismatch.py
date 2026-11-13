class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        sets = set([])
        dup = 0
        sums = 0  # 없는거 찾아내기위해
        for i in range(len(nums)):
            sums += i+1
            if nums[i] in sets:
                dup = nums[i]
            else:
                sets.add(nums[i])
        return [dup, sums-sum(nums)+dup]  # sums는 인덱스의 합계, 거기서 num의 합 빼주고 중복된 애는 다시 더해줌
