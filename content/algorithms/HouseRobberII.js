/**
 * @param {number[]} nums
 * @return {number}
 */
var rob = function(nums) {
    const doRob=(nums)=>{
        const robs = nums.slice(0, 1)
        for(let i=1; i<2; i++){
            robs.push(Math.max(nums[0], nums[1]));
        }
        for(let i=2; i<nums.length; i++){
            robs.push( Math.max(robs[Math.max(i-1)], robs[Math.max(i-2)]+nums[i]) );
        }
        return robs[robs.length-1];
    }
    if(nums.length <= 2){
        return Math.max(...nums)
    }
    return Math.max(doRob(nums.slice(0, nums.length-1)), doRob(nums.slice(1, nums.length)));
};
