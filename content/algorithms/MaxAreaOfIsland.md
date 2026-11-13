---
date: '2021-10-18'
---

```python
class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        totalLandCnt = [0]  # 각 섬의 땅 갯수들
        width = len(grid[0])
        height = len(grid)
        visited = [[False] * width for i in range(height)]

        def checkIsLand(i, j):
            cnt = 0
            if grid[i][j] == 1 and not visited[i][j]:
                visited[i][j] = True
                cnt += 1
                if i > 0:
                    up = checkIsLand(i - 1, j)
                    cnt += up
                if j > 0:
                    left = checkIsLand(i, j - 1)
                    cnt += left
                if i + 1 < height:
                    under = checkIsLand(i + 1, j)
                    cnt += under
                if j + 1 < width:
                    right = checkIsLand(i, j + 1)
                    cnt += right

                return cnt
            return cnt

        for i in range(height):
            for j in range(width):
                if grid[i][j] == 1:
                    if not visited[i][j]:
                        result = checkIsLand(i, j)
                        totalLandCnt.append(result)  # 재귀로 얻은 땅의 갯수 저장

        return max(totalLandCnt)

# 맨 왼쪽 위의 땅을 시작점으로 거기의 네 면을 재귀로 확인
# 방문한 적 있으면 pass
# 처음 방문이면 카운트 +1 하고  다 확인했으면 최종 땅 면적에 저장
```

```javascript
/**
 * @param {number[][]} grid
 * @return {number}
 */
var maxAreaOfIsland = function (grid) {
  const rowLen = grid.length;
  const colLen = grid[0].length;
  let maxCnt = 0;

  const counting = (row, col) => {
    let cnt = 0;
    if (
      row === -1 ||
      col === -1 ||
      row === grid.length ||
      col === grid[0].length ||
      grid[row][col] === 0
    )
      return 0;
    grid[row][col] = 0;
    cnt++;

    cnt +=
      counting(row - 1, col) +
      counting(row, col + 1) +
      counting(row + 1, col) +
      counting(row, col - 1);

    return cnt;
  };

  for (let row = 0; row < rowLen; row++) {
    for (let col = 0; col < colLen; col++) {
      if (grid[row][col] === 1) {
        const cnt = counting(row, col);
        maxCnt = cnt > maxCnt ? cnt : maxCnt;
      }
    }
  }
  return maxCnt;
};
```
