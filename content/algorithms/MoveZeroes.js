/**
 * @param {number[]} nums
 * @return {void} Do not return anything, modify nums in-place instead.
 */
var moveZeroes = function(nums) {
    let p = 0;  // 0 위치를 가리킬 포인터
    for (const i in nums){
        const num = nums[i];
        if(nums[p] === 0 && num !== 0){
            const temp = nums[p];
            nums[p] = nums[i]
            nums[i] = temp
        }
        if(nums[p] !== 0) p ++;
    }
};

/*
[two pointer]
제일 처음 나오는 0을 가리킬 포인터를 만듦
그리고 nums를 순회하면서 0이 아닌 숫자가 나왔을 때 0하고 위치를 바꾸고 포인터는 증가시킴
!!! 0의 포인터가 0이 아닐경우에만 증가시켜야함
*/
