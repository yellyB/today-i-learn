---
date: '2021-12-21'
---

```python
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        answer = [[]]
        for num in nums:
            for i in range(len(answer)):
                answer.extend([answer[i]+[num]])
        return answer
```

```javascript
/**
 * @param {number[]} nums
 * @return {number[][]}
 */
var subsets = function(nums) {
    const recursion=(idx, list)=>{
        if(idx === nums.length) return list;  // 끝까지 돌았다면 리턴
        const temp = list.map((item) => [...item,nums[idx]] )
        return recursion(idx+1, [...list, ...temp] );
    }
    
    return recursion(0, [[]]);
};
```
