---
date: '2022-05-26'
---

```python
class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        n = len(grid)
        memo = [[float('inf')] * n for _ in range(n)]  # 처음엔 inf 값으로 초기화
        visited = [[False] * n for _ in range(n)]
        stack = [(0,0,0)]  # (0,0)=현재위치랑 이전값
        dirs = [[-1,0], [0,-1], [0,1],[1,0]]
        
        while stack:
            # val = stack.pop()
            val = heapq.heappop(stack)
            row, col = val[1], val[2]
            if 0<=row<n and 0<=col<n and visited[row][col]==False:
                for r, c in dirs:
                    # (이전값, 현grid) 중 max를, 메모돼있는(처음엔 inf값인) 값과 비교해서 min값을 메모함
                    memo[row][col] = min(memo[row][col], max(grid[row][col], val[0]))
                    # stack.append((row+r,col+c,memo[row][col]))  # 다음 검사할 위치와 이전값이 될 현재 메모값
                    heapq.heappush(stack, (memo[row][col],row+r,col+c) )
                    # print(stack)
                visited[row][col] = True
            # if row==0and col==1:
                # break
        print(memo)
        
        
        return memo[-1][-1]
    
    # 다익스트라
    # https://namu.wiki/w/%EB%8B%A4%EC%9D%B5%EC%8A%A4%ED%8A%B8%EB%9D%BC%20%EC%95%8C%EA%B3%A0%EB%A6%AC%EC%A6%98
```

```javascript
/**
 * @param {number[][]} grid
 * @return {number}
 */
var swimInWater = function(grid) {
    const visited = new Set();
    let time = 0;
    let n = grid.length;
    
    // 각 칸마다 번호를 붙여서
    // 그 칸의 값이 적어도 time보다 작다면 수영가능
    // 값이 time보다 크다면 time을 1씩 늘려가면서 끝까지 갈 수 있을때까지 검사
    const dfs =(row, col)=>{
        if(0<=row && row<n && 0<=col && col<n && !visited.has(row*n+col) && grid[row][col] <= time){
            visited.add(row*n+col);
            for(const [r, c] of [[0,1],[1,0],[0,-1],[-1,0]]){
                dfs(row+r, col+c);
            }
        }
        return
    }
    
    while(!visited.has(n*n-1)){
        visited.clear();
        dfs(0,0);
        time ++;
    }
    
    return time-1;
};
```
