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
