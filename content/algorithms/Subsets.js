/**
 * @param {number[]} nums
 * @return {number[][]}
 */
var subsets = function(nums) {
    const recursion=(idx, list)=>{
        if(idx === nums.length) return list;  // 끝까지 돌았다면 리턴
        const temp = list.map((item) => [...item,nums[idx]] )
        return recursion(idx+1, [...list, ...temp] );
    }
    
    return recursion(0, [[]]);
};
