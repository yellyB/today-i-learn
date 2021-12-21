class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        # nums -> 반복문ㄱㄱ
        # => maxNums가 3칸 다 채워지면 거기서 젤 작은 값 반환
        # 숫자가 3개가 안채워졌다면 거기서 젤 큰 값 반환
        maxNums = []
        nums.sort(reverse=True)
        for num in nums:
            if num not in maxNums:
                maxNums.append(num)
            if len(maxNums) == 3:
                return min(maxNums)
        return max(maxNums)