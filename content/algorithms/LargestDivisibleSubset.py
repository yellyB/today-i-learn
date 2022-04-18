class Solution:
    def largestDivisibleSubset(self, nums: List[int]) -> List[int]:
        # sort를 안하면 문제가 [i-1]과 [i]는 조건을 만족했었는데 나중에 [i]랑 [i+n]했을 때 조건 만족안할수도
        nums.sort()
        
        dp = [[num] for num in nums]
        
        for i in range(len(nums)):
            for j in range(i):
                if nums[i]%nums[j] == 0 and len(dp[i])<=len(dp[j]): 
                    dp[i] = dp[j] + [nums[i]]  # [i]가 더 큰인덱스일테니(정렬해줘서) 큰애는 뒤에 붙여줌
                    
        return max(dp, key=len)
    
    """
    [위치 - 내부 반복문]
    1. if문에서 비교: 큰 수에서 작은 수 나눠야 0으로 떨어짐
        [i]가 [j]보다 큰 수일 경우만 체크될거임.
        이 if문을 통과했다면 [i]는 [j]보다 크다.
    2. 내부 반복문에서 길이비교하는 이유: [4,8,10,240] 케이스 방어
        [j]는 [i]보다 작기때문에 dp[j]에는 이미 뭔가의 값이 저장되어있음(j가 한때 과거의 i였으니까)
        그 개수가 현재의 i인 경우보다 커야지 갱신하는 의미가 있음.
        dp[j]에는 어차피 더이상 추가될 값이 없어서 걔가 최종값임
        근데 dp[i]는 아직 더 가능성이 큰 아이임. 이미 끝난애들로 가능성있는애를 비교해줘야지
        
    """
