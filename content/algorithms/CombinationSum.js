/**
 * @param {number[]} candidates
 * @param {number} target
 * @return {number[][]}
 */
var combinationSum = function(candidates, target) {
    const func=(sums, idx, curr, res)=>{
        if(idx == candidates.length) return res;
        for(let i=idx; i<candidates.length; i++){
            const tempSum = sums+candidates[i]
            if(tempSum == target){
                res.push([...curr, candidates[i]]);
            }else if(tempSum < target){
                func(tempSum, i, [...curr, candidates[i]], res)
            }
        }
        return res
        
    }
    return func(0, 0, [], [])  // (지금까지 합계, 현재 인덱스, 현재까지 선택 목록, 최종정답)
};
