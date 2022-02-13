/**
 * @param {number[]} numbers
 * @param {number} target
 * @return {number[]}
 */
var twoSum = function(numbers, target) {
    let low = 0;
    let high = numbers.length - 1;
    while(low < high){
        const sums = numbers[low] + numbers[high];
        if(sums === target) break
        else if(sums < target) low ++;
        else high --
    }
    return [low+1, high+1]
};

/*
[two pointer]
오름차순 정렬되었기 때문에 두 포인터값의 합이 타겟과 비교해서 큰지 작은지에 따라 증감가능
합계가 타겟보다 작으면 작은숫자쪽 포인터를 증가, 반대면 큰 숫자쪽 포인터 감소시킴
*/
