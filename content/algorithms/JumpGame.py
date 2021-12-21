class Solution:
    def canJump(self, nums: List[int]) -> bool:
    # 한 방법이라도 끝까지 가면 True ==> 전부 불가능하면 False란 뜻
    # 불가능한 경우:중간에 0을 만났는데 걜 못뛰어넘음
    # 0을 만났을때 얘를 뛰어넘을 수 있는지 보면됨
        maxIdx = nums[0]
        for i in range(len(nums)-1):
            if nums[i] == 0 and maxIdx <= i:
                return False
            maxIdx = max(maxIdx, i+nums[i])

        # 다 돌고 맨마지막 인덱스보다 최대 점프위치가 크면 True
        if len(nums)-1 <= maxIdx:
            return True
        else:
            return False