/**
 * @param {number[]} nums
 * @return {number[][]}
 */
var subsetsWithDup = function(nums) {
    nums.sort();
    
    const used = [];  // 이미 추가한 애들 저장
    
    const recursion=(idx, list)=>{
        if(idx === nums.length) return list;  // 끝까지 돌았다면 리턴
      
        // filter로 used에 아직 안들어간애들만 map 돌림
        const temp = list.filter((item) => !used.includes(String([...item,nums[idx]])) ).map((item) => { 
            used.push(String([...item,nums[idx]]))
            return [...item,nums[idx]];
        } )
        
        return recursion(idx+1, [...list, ...temp] );
    }
    
    return recursion(0, [[]]);
};
