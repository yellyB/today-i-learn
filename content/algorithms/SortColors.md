---
date: '2022-04-07'
---

```python
class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # red=0 white=1 blue=2
        for i in range(len(nums)):
            # red(0)은 앞부터 정렬하고
            red = i+1
            while red<len(nums) and nums[red] != 0:
                red += 1
            if red<len(nums):
                nums[i], nums[red] = nums[red], nums[i]
            
            # blue(2)는 뒤부터 정렬
            blue = len(nums)-1-i
            while blue>=0 and nums[blue] != 2:
                blue -= 1
            if blue>=0:
                nums[len(nums)-1-i], nums[blue] = nums[blue], nums[len(nums)-1-i]
```

```javascript
/**
 * @param {number[]} nums
 * @return {void} Do not return anything, modify nums in-place instead.
 */
var sortColors = function(nums) {
    let red = 0;
    let blue = nums.length-1;
    for(let i=0; i<nums.length; i++){
        // 0일경우를 먼저 swap하면 [1,2,0]케이스 방어 불가
        while(nums[i]==2 && i<blue){
            let temp = nums[i]
            nums[i] = nums[blue]
            nums[blue] = temp
            blue --;
        }
        while(nums[i]==0 && red<i){
            let temp = nums[i]
            nums[i] = nums[red]
            nums[red] = temp
            red ++;
        }
    }
};
```
