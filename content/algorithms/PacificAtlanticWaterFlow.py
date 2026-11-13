class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        rowLen = len(heights)
        colLen = len(heights[0])
        p_land = set()
        a_land = set()
        
        def dfs(i, j, land):
            land.add((i, j))
            for x, y in ((i+1, j), (i, j+1), (i-1, j), (i, j-1)):
                # 1. 범위 벗어나지 않고  2. 이전 셀보다 크.같  3. 중복이 아닌
                if (0 <= x < rowLen and 0 <= y < colLen and heights[x][y] >= heights[i][j] and (x, y) not in land):
                    dfs(x, y, land)
        
        for i in range(rowLen):
            dfs(i, 0, p_land)  # 왼
            dfs(i, colLen-1, a_land)  # 오
        for j in range(colLen):
            dfs(0, j, p_land)  # 위
            dfs(rowLen-1, j, a_land)  # 아래

        return list(p_land & a_land)
        
        
                
