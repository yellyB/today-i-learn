/**
 * @param {number[]} nums
 * @return {number[]}
 */
var sortedSquares = function(nums) {
    let left = 0;
    let right = nums.length-1;
    const answer = []
    while(left <= right){
        if(Math.abs(nums[left]) > Math.abs(nums[right])){
            answer.push(Math.pow(nums[left], 2));
            left ++
        }else{
            answer.push(Math.pow(nums[right], 2));
            right --
        }
    }
    return answer.reverse()
};


/*
 [two pointer]
 asc 정렬되어 있기 때문에 맨 앞 혹은 맨 뒤의 숫자의 제곱이 배열중 가장 큰 숫자일거임
 1. 맨앞, 맨뒤를 포인터로 잡고 큰수부터 answer에 담는다.
 2. 마지막에 reverse()로 뒤집기
 
 또 다른 방법:
 맨 처음에 Array(nums.length)로 배열을 미리 만들고
 i로 포인터를 하나 더 만들어서 뒤부터 차례대로 담아서 마지막에 뒤집기 생략하기
*/
