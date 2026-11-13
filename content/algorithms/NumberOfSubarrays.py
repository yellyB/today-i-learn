class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        res = cnt = 0
        l = 0
        restOddCnt = k
        
        for r in range(len(nums)):
            if nums[r] % 2:
                restOddCnt -= 1
                cnt = 0  # 새로운 홀수 만나면 저번 루프 돌았던 값 초기화
            
            while restOddCnt == 0:
                cnt += 1
                restOddCnt += nums[l] % 2
                l += 1
            res += cnt  # 모든 경우의 수 계산해야 하기 때문에 누적 값을 계산해줘야 함

        return res
