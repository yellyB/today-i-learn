class Solution:
    def longestArithSeqLength(self, nums: List[int]) -> int:
        dp = {}  # diff를 key로 value엔 개수를 저장
        for i in range(len(nums)):
            for j in range(i):
                diff = nums[j]-nums[i]
                if (j, diff) in dp:
                    dp[(i, diff)] = dp[(j, diff)] + 1
                else:
                    dp[(i, diff)] = 2  # 두개를 비교한거니까 처음엔 2부터 시작
        return sorted(dp.values())[-1]
    
    # 내부 for문에서 i까지 돌 때, diff가 동일한 [j]가 있다면 현재 기준점인 [i]에 누적해서 저장해야함
    # dict에서 키를 그냥 diff만 잡으면 문제인게, 지난 subsequence에서 이어서 누적히야 하는데
    # 그냥 diff만 같은 애들이 전부 쌓이게 됨
    
