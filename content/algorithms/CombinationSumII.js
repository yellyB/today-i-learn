/**
 * @param {number[]} candidates
 * @param {number} target
 * @return {number[][]}
 */
var combinationSum2 = function(candidates, target) {
    const func=(sums, can, curr, res)=>{
        let i = 0;
        while(i<can.length){
            const tempSum = sums + can[i];
            if(tempSum == target){
                res.push([...curr, can[i]]);
            }else if(tempSum < target){
                func(tempSum, can.slice(i+1, can.length), [...curr, can[i]], res);
            }
            while(i+1<can.length && can[i] == can[i+1]) i++;  // 중복 제거 위해
            i++;
        }
        return res;
    }
    candidates.sort();  // 중복 제거 위해
    return func(0, candidates, [], []);
};

/* combination Sum 에서 중복제거가 추가된 문제인데
    중복 제거 위해 candidates를 정렬 한 후
    while문을 돌 때 다음번 요소랑 같으면 i를 계속 증가시킴.
*/
