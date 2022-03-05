/**
 * @param {number[]} arr
 * @return {number}
 */
var sumOddLengthSubarrays = function(arr) {
    let sum = 0;
    for(let start=0; start<arr.length; start++){
        let tempSum = 0;
        for(let end=start; end<arr.length; end++){
            tempSum += arr[end];
            if((end - start)%2 == 0){
                sum += tempSum;
            }
        }
    }
    
    return sum
};

/*
    시작지점과 끝지점 두가지 이용해서
    끝-시작  차이가 짝수면 subArray가 홀수 개 라는 뜻
*/
