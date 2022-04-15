class Solution:
    def maxSizeSlices(self, slices: List[int]) -> int:
        lens = len(slices)  # 여기서 ÷3하면 총 몇개 선택할수 있는지 나옴
        
        def getMax(slices):
            dp = [[0]*(lens//3+1) for _ in range(lens)]  # ÷3한거에 1더해주는건 걍 인덱스랑 개수 일치시키려고
            # print(dp)

            maxVal = max(slices[0], slices[1])
            
            # 첫빠따랑 둘째는 이전 선택 존재X
            dp[0][1] = slices[0]
            dp[1][1] = maxVal
            
            
            for i in range(2, lens-1):
                for cnt in range(1, lens//3+1):
                    # print(i,cnt)
                    dp[i][cnt] = max(dp[i-2][cnt-1]+slices[i], dp[i-1][cnt])
                maxVal = max(maxVal, dp[i][-1])
            
            print(dp)
            return maxVal
        
        return max( getMax(slices[:-1]), getMax(slices[1:]) )
        
        
        
        """
        이번에 안되면 자살함 Tlqkf
        [1,2,3,4,5,6] 에서 이 전 선택을 기반으로 총 합계가 바뀌는건 3부터임.
        [1,2]까지는 그냥 기록용
        
        근데 문제는 3을 선택할지 말지 결정할 때 3을 단독으로 선택하는 경우와 1을 선택하고 3을 선택하는 두가지가 있음
        4도 마찬가지 4/1+4/2+4 의 경우가 있고 뒤에 쭉 다 이럼
        
        근데 3을 선택한 결과를 기반으로 뒤에서 이걸 이용해 dp를 기록해야 하는데
        이렇게 경우가 여러가지고 전부 있을 수 있는 경우라면 뭘 저장해야 하는지 모르게되어버림
        
        그래서 이중배열을 사용함
        이중배열로 [0][x]은 기존 dp 방식과 똑같은데 [i][1]에는 몇 개의 조각을 선택했나 저장할거임
        예를들어 dp[2][1]=4 라면 slices의 [2]조각을 1개 선택했을 경우의 최고값이 4라는 얘기
        
        """
