---
date: '2022-05-12'
---

```python
class Solution:
    def canBeEqual(self, target: List[int], arr: List[int]) -> bool:
        return sorted(target) == sorted(arr)
```

```javascript
/**
 * @param {number[]} target
 * @param {number[]} arr
 * @return {boolean}
 */
var canBeEqual = function(target, arr) {
    target.sort((a,b)=>a-b);
    arr.sort((a,b)=>a-b);
    for (let i=0; i<target.length; i++){
        if(target[i] !== arr[i]) return false;
    }
    return true;
};
```
