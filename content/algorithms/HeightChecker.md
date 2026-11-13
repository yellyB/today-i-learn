---
date: '2022-05-12'
---

```python
class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        cnt = 0
        for i, j in zip(heights, sorted(heights)):
            if i != j: cnt += 1
            
        return cnt
```

```javascript
/**
 * @param {number[]} heights
 * @return {number}
 */
var heightChecker = function(heights) {
    let cnt = 0;
    const sorted = [...heights].sort((a,b)=>a-b);
    for(let i=0; i<heights.length; i++){
        if(heights[i] !== sorted[i]) cnt ++;
    }
    return cnt
};
```
