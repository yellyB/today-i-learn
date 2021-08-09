class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        answer = []
        for num in nums:
            # 짝수면 맨 앞에, 홀수면 맨 뒤에 붙임
            if num % 2 == 0:
                answer.insert(0,num)
            else:
                answer.append(num)
        return answer