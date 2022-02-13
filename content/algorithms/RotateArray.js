/**
 * @param {number[]} nums
 * @param {number} k
 * @return {void} Do not return anything, modify nums in-place instead.
 */
var rotate = function(nums, k) {
    const reverse = (left, right, arr) => {
        while (left < right){
            const temp = arr[left];
            arr[left] = arr[right]
            arr[right] = temp
            
            left ++;
            right --;
        }
    }
    
    if(k>nums.length) k = k % nums.length;  // k가 길이보다 더 길경우 처리
    
    reverse(0, nums.length-1, nums);  // 1. 전체 뒤집기
    reverse(0, k-1, nums);  // 2. 0 ~ k 뒤집
    reverse(k, nums.length-1, nums);  // 3. k ~ 끝 뒤집
    
};


/*
[two pointer]
*파이썬으로 풀때는 k만큼만 잘라서 앞에 붙이는 방법 사용
이번 방식은 투포인터로 품
*/
