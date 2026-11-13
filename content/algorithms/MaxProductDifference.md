---
date: '2021-07-06'
---

```python
class Solution:
    def maxProductDifference(self, nums: List[int]) -> int:
        nums.sort(reverse=True)
        return nums[0]*nums[1] - nums[len(nums)-2] * nums[len(nums)-1]
```
