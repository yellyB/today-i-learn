/**
 * @param {number[][]} people
 * @return {number[][]}
 */
var reconstructQueue = function(people) {
    const sorting=(a, b)=>{
        if(a[0]==b[0]) return a[1]-b[1];  // 첫 값이 같으면 두번째로 정렬
        else return b[0]-a[0];  // 그외엔 첫값으로 내림차순 정렬
    }
    const answer = [];
    people.sort(sorting);
    
    for(const p of people){
        answer.splice(p[1], 0, p);  // 앞에 몇명 있는지 데이터를 인덱스로해서 추가해줌
    }
    
    return answer
};
