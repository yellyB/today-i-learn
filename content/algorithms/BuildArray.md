---
date: '2021-07-07'
---

```python
class Solution:
    def buildArray(self, nums: List[int]) -> List[int]:
        newList = []
        for num in nums:
            newList.append(nums[num])
        return newList
```
