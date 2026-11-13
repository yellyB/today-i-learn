---
date: '2021-10-14'
---

```python
class Solution:
    def countKDifference(self, nums: List[int], k: int) -> int:
        answer = 0
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                if abs(nums[i] - nums[j]) == k:
                    answer += 1
        return answer
```
