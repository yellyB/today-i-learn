/**
 * @param {number[]} nums
 * @param {number} k
 * @return {number[]}
 */
var topKFrequent = function(nums, k) {
    const map = new Map();
    for(let i=0; i<nums.length; i++){
        map.set(nums[i], (map.get(nums[i]) || 0) + 1);
    }
    
    const arr = [...map];
    
    return arr.sort((a,b) => b[1]-a[1]).map((item) => item[0]).slice(0, k)
};
