/**
 * @param {number[]} nums
 * @return {number}
 */
var majorityElement = function(nums) {
    const freq = new Map();
    
    for(const n of nums){
        freq.set(n, (freq.get(n)||0) + 1);
    }
    
    return [...freq].sort((a,b)=>b[1]-a[1])[0][0]
};
