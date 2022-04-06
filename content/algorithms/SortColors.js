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
    
    
