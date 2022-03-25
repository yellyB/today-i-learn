/**
 * @param {number[]} difficulty
 * @param {number[]} profit
 * @param {number[]} worker
 * @return {number}
 */
var maxProfitAssignment = function(difficulty, profit, worker) {
    let total = 0;
    const diffAndPro = [];
    
    // 1. 어려움과 이익을 묶어서 정렬할거임. 이익 높은 업무부터 체크해야함
    for(let i=0; i<profit.length; i++){
        diffAndPro.push([difficulty[i],profit[i]]);
    }
    diffAndPro.sort((a,b)=>b[1]-a[1]);
    
    
    // 2. 노동자의 능력내에서 가능한 일 찾기
    worker.sort((a,b)=>b-a);  // 능력 좋은 노동자부터 체크
    let jobIdx = 0;
    let workIdx = 0;
    while(jobIdx < diffAndPro.length && workIdx < worker.length){
        // 노동자 능력이 낮으면 다음 업무 확인하러
        if(worker[workIdx] < diffAndPro[jobIdx][0]){
            jobIdx ++;  // 아쉽지만 다음 업무 확인 ㄱㄱ
        }else{
            total += diffAndPro[jobIdx][1];  // 능력 내의 일이면 정답에 추가
            workIdx ++;  // 다음 노동자 확인 ㄱㄱ
        }
    }
    

    return total;
};
