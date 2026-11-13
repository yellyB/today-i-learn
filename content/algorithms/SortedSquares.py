class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        left, right = 0, len(nums) - 1
        answer = []

        while left <= right:
            if abs(nums[left]) >= abs(nums[right]):
                answer.append(pow(nums[left], 2))
                left += 1
            else:
                answer.append(pow(nums[right], 2))
                right -= 1
        return sorted(answer)

        # 절대값이 크면 제곱수가 크니까 절대값으로 비교하면 됨
        # 맨 앞, 맨 뒤 중 절대값이 젤 큰 수가 있을거임