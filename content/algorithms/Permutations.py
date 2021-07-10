class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        if len(nums) == 1:
            return [nums]
        nums.sort()
        answer = []
        answer.append(nums[:])
        while True:
            i = len(nums) - 2
            while nums[i] > nums[i+1]:  # 뒤 숫자가 큰게 나올때까지 i--
                i -= 1
                if i == -1:  # nums가 내림차순 정렬되었단 뜻. 함수 종료
                    return answer
            j = len(nums) - 1
            while j > i:
                if nums[i] < nums[j]:
                    nums[i], nums[j] = nums[j], nums[i]
                    nums = nums[:i+1] + sorted(nums[i+1:])
                    answer.append(nums[:])
                    break
                j -= 1