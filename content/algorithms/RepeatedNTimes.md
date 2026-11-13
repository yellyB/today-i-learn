---
date: '2021-10-15'
---

```python
class Solution:
    def repeatedNTimes(self, nums: List[int]) -> int:
        n = len(nums) // 2
        for num in nums:
            cnt = nums.count(num)
            if cnt == n:
                return num
```
