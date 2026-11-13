class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        answer = []
        i = 0
        start, end = 0, len(nums)
        while i < end:
            left, right = i+1, end-1
            while left < right:
                sums = nums[i] + nums[left] + nums[right]
                
                # 셋을 더해서 0이면 정답에 추가
                if sums == 0:
                    answer.append([nums[i], nums[left], nums[right]])
                    
                    # 중복 제거하기 위해: 현 숫자가 다음숫자랑 같으면 패스
                    while left<right and nums[left] == nums[left+1]:
                        left += 1
                        
                    left += 1
                    right -= 1
                    
                elif sums < 0:
                    left += 1
                else:
                    right -= 1
            
            # 중복 제거하기 위해: 현 숫자가 다음숫자랑 같으면 패스
            while i+1 < right and nums[i] == nums[i+1]:
                i += 1
            i += 1
        
        return answer
    
    # 처음과 끝을 정하고(0, len) 그 안에서 i를 하나씩 증가시키는데
    # 이 i는 중간 숫자임.
    
    # 그 앞과 뒤의 숫자는 left와 right로 양 끝에서 출발하고
    # 하나씩 증가/감소 시킬거임
    
    # left나 i를 증가시키다가 다음 숫자가 현재 숫자랑 같다면 중복이니까
    # 이럴 경우에는 건너뜀
