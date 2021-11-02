class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:
        answer = 0
        nums.sort()
        i = 0
        while i < len(nums):
            answer += nums[i]
            i += 2
        return answer

    # 두개씩 짝지은다음 그 중 작은걸 선택하는거니까
    # 젤큰수,2번째큰수 / 3번째큰수,4번째큰수  => 이렇게 짝지어서 큰수가 최대한 덜 버려지게