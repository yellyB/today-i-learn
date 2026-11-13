---
date: '2021-11-05'
---

```python
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        rowLen = len(grid)
        colLen = len(grid[0])
        cnt = 0

        def isLand(i, j):
            if 0 > i or i >= rowLen or 0 > j or j >= colLen:
                return
            if grid[i][j] == "1":
                grid[i][j] = 1

                isLand(i - 1, j)
                isLand(i, j - 1)
                isLand(i + 1, j)
                isLand(i, j + 1)

        for i in range(rowLen):
            for j in range(colLen):
                if grid[i][j] == "1":
                    isLand(i, j)
                    cnt += 1

        return cnt
```

```javascript
/**
 * @param {character[][]} grid
 * @return {number}
 */
var numIslands = function(grid) {
    const rowLen = grid.length;
    const colLen = grid[0].length;
    let cnt = 0;
    const getCount = (i, j) => {
        if(i < 0 || j < 0 || i >= rowLen || j >= colLen) return
        if(grid[i][j] == '1'){
            grid[i][j] = '0';
            getCount(i, j+1);
            getCount(i, j-1);
            getCount(i+1, j);
            getCount(i-1, j);
            
        }
    }
    
    for(let i=0; i<rowLen; i++){
        for(let j=0; j<colLen; j++){
            if(grid[i][j] == '1'){
                getCount(i, j);
                cnt ++;
            }
            
        }
    }
    
    
    return cnt
};
```
