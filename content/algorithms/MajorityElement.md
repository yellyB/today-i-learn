---
date: '2022-03-30'
---

```python
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        freq = {}
        for n in nums:
            if n in freq: freq[n] += 1
            else: freq[n] = 1
        
        sort = sorted(freq.items(), key=lambda x:x[1], reverse=True)
        
        
        return sort[0][0]
```

```javascript
/**
 * @param {number[]} nums
 * @return {number}
 */
var majorityElement = function(nums) {
    const freq = new Map();
    
    for(const n of nums){
        freq.set(n, (freq.get(n)||0) + 1);
    }
    
    return [...freq].sort((a,b)=>b[1]-a[1])[0][0]
};
```
