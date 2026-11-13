---
date: '2021-11-08'
---

```python
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        orinLen = len(nums)
        nums = set(nums)
        return orinLen != len(nums)

    # 원래 len과 중복 제거후의 len 비교. 중복되는게 있다면 다르겠찌?
```

```javascript
/**
 * @param {number[]} nums
 * @return {boolean}
 */
var containsDuplicate = function(nums) {
    const checked = [];
    for (const n of nums){
        if(checked.indexOf(n) !== -1){
            return true;
        }
        checked.push(n);
    }
    return false;
};
```
