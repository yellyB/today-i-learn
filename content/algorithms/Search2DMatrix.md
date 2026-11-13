---
date: '2021-11-20'
---

```python
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rowLen = len(matrix)
        colLen = len(matrix[0])
        start, end = 0, (rowLen * colLen)
        while start < end:
            mid = (start + end) // 2  # 여기서 몫은 row고 나머지는 col위치임
            val = matrix[mid // colLen][mid % colLen]
            if val == target:
                return True
            elif val < target:
                start = mid + 1
            elif val > target:
                end = mid
        return False
```

```javascript
/**
 * @param {number[][]} matrix
 * @param {number} target
 * @return {boolean}
 */
var searchMatrix = function(matrix, target) {
    const rowLen = matrix.length;
    const colLen = matrix[0].length;
    let s = 0;
    let e = rowLen * colLen;
    while (s < e){
        const mid = Math.floor((s+e)/2);
        const midVal = matrix[Math.floor(mid/colLen)][mid%colLen]
        if(midVal == target) return true
        else if(midVal < target) s = mid+1
        else e = mid-1
    }
    return false
};
```
