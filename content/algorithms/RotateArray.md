---
date: '2021-11-09'
---

```python
class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        length = len(nums)

        if length < k:
            k = k % length

        cutIdx = length - k  # 잘라야 하는 기준 인덱스

        nums[:] = nums[cutIdx:] + nums[:cutIdx]

        # k번 만큼 맨뒤꺼를 맨 앞으로 옮기는건 만약 k가 3이라면 뒤에서 3개만큼을 앞으로 옮기면 됨
        # k가 len보다 클 때만 처리해주면 끝
```

```javascript
/**
 * @param {number[]} nums
 * @param {number} k
 * @return {void} Do not return anything, modify nums in-place instead.
 */
var rotate = function(nums, k) {
    const reverse = (left, right, arr) => {
        while (left < right){
            const temp = arr[left];
            arr[left] = arr[right]
            arr[right] = temp
            
            left ++;
            right --;
        }
    }
    
    if(k>nums.length) k = k % nums.length;  // k가 길이보다 더 길경우 처리
    
    reverse(0, nums.length-1, nums);  // 1. 전체 뒤집기
    reverse(0, k-1, nums);  // 2. 0 ~ k 뒤집
    reverse(k, nums.length-1, nums);  // 3. k ~ 끝 뒤집
    
};


/*
[two pointer]
*파이썬으로 풀때는 k만큼만 잘라서 앞에 붙이는 방법 사용
이번 방식은 투포인터로 품
*/
```
