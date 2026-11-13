class Solution:
    def minSubsequence(self, nums: List[int]) -> List[int]:
        total = sum(nums) // 2  # 전체 요소 합%2. 얘보다는 큰 부분배열 알아내야함
        sums = 0  # 젤 큰수부터 더해나갈 변수
        answer = []
        for num in sorted(nums, reverse=True):
            sums += num
            answer.append(num)
            if total < sums:
                return answer
        return []
        
