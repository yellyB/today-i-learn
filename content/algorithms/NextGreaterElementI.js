/**
 * @param {number[]} nums1
 * @param {number[]} nums2
 * @return {number[]}
 */
var nextGreaterElement = function(nums1, nums2) {
    const findIdxInNums2 = (num) => {
        for(let i=0; i<nums2.length; i++){
            if(nums2[i] == num){
                return i
            }
        }
        return -1
    }
    
    const findNextMaxNum = (num, idx) => {
        if(idx === -1) return -1
        for(let i=idx+1; i<nums2.length; i++){
            if(nums2[i] > num){
                return nums2[i]
            }
        }
        return -1
    }
    
    const answer = []
    
    for(let i=0; i<nums1.length;i++){
        const idxInNums2 = findIdxInNums2(nums1[i]);
        answer.push(findNextMaxNum(nums1[i], idxInNums2))
    }
    
    return answer
    
};
