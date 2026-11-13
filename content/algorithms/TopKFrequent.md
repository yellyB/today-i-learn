---
date: '2022-03-30'
---

```python
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = {}
        for n in nums:
            if n in freq: freq[n] += 1
            else: freq[n] = 1
        
        sort = sorted(freq.items(), key=lambda x:x[1], reverse=True)
        
        answer = []
        for i in range(k):
            answer.append(sort[i][0])
        
        return answer
```

```javascript
/**
 * @param {number[]} nums
 * @param {number} k
 * @return {number[]}
 */
var topKFrequent = function(nums, k) {
    const map = new Map();
    for(let i=0; i<nums.length; i++){
        map.set(nums[i], (map.get(nums[i]) || 0) + 1);
    }
    
    const arr = [...map];
    
    return arr.sort((a,b) => b[1]-a[1]).map((item) => item[0]).slice(0, k)
};
```
