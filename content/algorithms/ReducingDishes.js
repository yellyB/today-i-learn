/**
 * @param {number[]} satisfaction
 * @return {number}
 */
var maxSatisfaction = function(satisfaction) {
    satisfaction.sort((a,b)=>b-a);
    const sats = [satisfaction[0]];
    let total = satisfaction[0];  // 접시 만족도 각각. 한칸이동할때마다 한번씩 더 더해줄거
    for(let i=1; i<satisfaction.length; i++){
        total += satisfaction[i];
        sats.push( sats[i-1] + total);  // 이전 합계에 현재접시더해서 그걸 이전의 합계랑 합해줌
    }
    return Math.max(...sats)<0?0:Math.max(...sats);
};
