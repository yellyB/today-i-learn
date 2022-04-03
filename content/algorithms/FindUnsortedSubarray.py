class Solution:
    def findUnsortedSubarray(self, nums: List[int]) -> int:
        
        start, end = 0, len(nums)
        
        # sort해야하는 제일 앞 인덱스랑 제일 끝 인덱스 찾기
        for i in range(len(nums)-1):
            if nums[i] > nums[i+1]:
                start = i
                break
        
        for i in range(len(nums)-1, start, -1):
            if nums[i-1] > nums[i]:
                end = i
                break
        
        # 정렬할거없으면 리턴
        if start == 0 and end == len(nums): return 0
        
        # start와 end를 잡았는데 여기까지 하고 끝내면 [2,3,3,2,4] 같은 애들 못잡아냄
        # [2:3]까지만 잡게되는데 [1]까지 정렬이 필요하다.
        # 그러면 일단 지금까지 잡은 범위중에서 최소값과 최고값을 구한다음
        # 범위의 앞에 최소값보다 큰애가 있다면 걔도 범위에 포함시켜 줌. 최대도 마찬가지
        haveToSort = nums[start:end+1]
        minNum = min(haveToSort)
        maxNum = max(haveToSort)
        
        while 0<start and minNum<nums[start-1]: start -= 1
        while end<len(nums)-1 and nums[end+1]<maxNum: end += 1
        
        return end-start+1
        
                
