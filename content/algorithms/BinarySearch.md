---
date: '2021-11-08'
---

```python
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums) - 1
        while left <= right:
            center = left + (right - left) // 2  #
            if nums[center] == target:
                return center
            elif nums[center] < target:
                left = center + 1
            elif nums[center] > target:
                right = center - 1

        return -1

    # 주제에 맞게 풀기: 가운데 있는 값이 찾는 값인지 비교 -> 아니라면 대,소 비교해서 왼쪽포인터 혹은 오른쪽포인터를 1씩 조절
    #                 다시 가운데 값을 구해서 비교.
```

```javascript
/**
 * @param {number[]} nums
 * @param {number} target
 * @return {number}
 */
var search = function (nums, target) {
  let start = 0;
  let end = nums.length - 1;

  while (start <= end) {
    const mid = Math.round((start + end) / 2);
    if (nums[mid] == target) {
      return mid;
    } else if (nums[mid] < target) {
      start = mid + 1;
    } else {
      end = mid - 1;
    }
  }
  return -1;
};

/*

[이진 탐색]
nums가 오름차순으로 주어지기 때문에 이진탐색 알고리즘 사용할 수 있음
왼, 오를 중간값으로 대체하면서 원하는 타겟넘버를 찾아나간다.

*/
```
