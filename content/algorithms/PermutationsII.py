class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        answer = []
        targetLen = len(nums)
        def func(path, counter):
            if len(path) == targetLen:
                answer.append(path)
            for x in counter:
                if counter[x] > 0:  # counter가 1이상일때만, 다 썼으면 0이니까 걍 넘어갈거임
                    # 남은갯수 하나씩 빼줘서 다음 회차로 넘김. 넘겨주고선 원복
                    counter[x] -= 1
                    func(path+[x], counter)
                    counter[x] += 1
                    
        func([], Counter(nums))
        return answer
