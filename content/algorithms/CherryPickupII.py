class Solution:
    def cherryPickup(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        
        # grid를 가로로 col의 칸만큼 쪼개준 dp를 만듦
        dp = [[[0]*n for _ in range(n)] for __ in range(m)]
        
        
        # dp에 저장할 최고값 찾아주기
        def getValue(row, col1, col2):
            maxVal = 0
            for c1 in [-1, 0, 1]:
                for c2 in [-1, 0, 1]:
                    if 0<=col1+c1<n and 0<=col2+c2<n:
                        maxVal = max(maxVal, dp[row+1][col1+c1][col2+c2])
            return maxVal
        
        # row를 거꾸로 돌려야함
        for row in range(m-1, -1, -1):
            for col1 in range(n):
                for col2 in range(n):
                    total = 0
                    if col1 != col2:
                        total += grid[row][col1] + grid[row][col2]
                        
                        # 마지막 row는 아랫줄이 없으니 패스
                        if row < m-1:
                            total += getValue(row, col1, col2)
                            
                    dp[row][col1][col2] = total
        
        return dp[0][0][-1]  # 로봇1위치 리턴
                        

    '''
    1. row 거꾸로 이유
        로봇들은 row의 [0]에서 시작함. 그것도 첫줄의 양 끝에서 시작함
        그렇기때문에 row를 순서대로 돌려서 dp의 마지막줄을 리턴하려고 하면
        로봇이 어디서 시작했는지는 고려하지 않고 dp를 메모이제이션 해나가기 때문에
        원하는 값이 안나올 수도 있음.
        그래서 row를 거꾸로 돌린다음 마지막 dp를 리턴할 때 로봇의 시작 위치를 리턴해주는것.
          ㄴ [0][0][-1]은 로봇1의 위치를 리턴하는것. 로봇2위치를 리턴해도 됨
    2. dp 설명
        원래의 grid를 쪼갤건데 각 row를 가로로 column만큼씩 쪼개줄거임
        만약 3X3그리드였다면 dp로 9x3이 될거임
        이렇게 하는 이유는 각 row(colXcol인)에 로봇 두개가 움직였을때의 최고값을 저장할거라서.
        
        예시1처럼 4X3이라할때 쪼갠후의 row는 col인 3만큼 쪼개져서 3X3이 되어있을텐데
        여기에 각각 A,B,C라고 x축과 y축 모두에 이름을 붙인다 해보자
        A,A에는 말그대로 로봇1이 A로 가고 로봇2가 A로 간경우.
        A,B에는 로봇1 - A로 가고 로봇2 - B로 가고
        A,C에는 로봇1 - A로 로봇2 - C로 가는 경우.... 를 저장할거임
        겹치는 부분은 가면 안되니까 그냥 그 위치의 값을 0으로 해주면 어차피 MAX()에서 선택안됨
        
        제일 첫 순서인 row의 마지막줄은 위와 같이 하고
        그 윗줄부터는 이전에 구한 dp값을 이용하는데,
        이때 현재 구하려는 dp의 컬럼 위치와 인접한곳만 가져와서 연산할수 있음.
    
        
    '''
