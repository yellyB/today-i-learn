/**
 * @param {number[]} nums
 * @return {number}
 */
var triangleNumber = function(nums) {
    let cnt = 0;
    const len = nums.length;
    nums.sort((a,b)=>b-a);
    for(let a=0; a<len; a++){
        let b = a+1;  // 두번째 큰 수
        let c = len-1;  // 젤 작은 수
        while(b < c){
            if(nums[a] < nums[b]+nums[c]){
                cnt += (c-b);
                b ++;  // 둘큰수 더 줄여보기
            }else{
                c --;  // 삼각형실패면 젤 작은 수 키워보기
            }
        }
    }
    return cnt
};
