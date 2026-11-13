/**
 * @param {number[]} nums
 * @param {number} k
 * @return {number}
 */
var findKthLargest = function(nums, k) {
    const findPivot=(arr, l, r)=>{
        let i = l+1;
        let j = r;
        let pivot = arr[l];
        while(true){
            while(arr[i] >= pivot) i ++;
            while(pivot > arr[j] && i<=j) j --;
            // 여기에서 j는 pivot의 중간 지점의 바로 왼편에 위치해야한다.
            // 왜냐하면 j랑 pivot(인덱스0번)이랑 swap할거라서 pivot보다 작은 뭉탱이의 끝 지점을 가리켜야하기때문
            // (but 이문제에서는 reverse정렬해야해서 작은,큰 이 반대임)
            if(i<j){
                let temp = arr[i];
                arr[i] = arr[j];
                arr[j] = temp;   
            }else{
                break;
            }
        }
        arr[l] = arr[j];
        arr[j] = pivot;
        return j;
    }
    
    const quickSort=(arr, l, r)=>{
        if(l < r){
            let pivot = findPivot(arr, l, r);
            quickSort(arr, l, pivot-1);
            quickSort(arr, pivot+1, r);
        }
        return arr;
    }
    
    return quickSort(nums, 0, nums.length-1)[k-1];
};
