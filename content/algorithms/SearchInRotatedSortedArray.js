/**
 * @param {number[]} nums
 * @param {number} target
 * @return {number}
 */
var search = function(nums, target) {
    let low = 0;
    let high = nums.length-1;
    while(low<high){
        let mid = Math.floor((low + high) / 2);
        let m = nums[mid];
        if(m === target) return mid;
        // low ~ mid가 로테이션 부분이 아니면?
        if(nums[low] <= m){
            if(nums[low] <= target && target < m){  // 타겟마저 로테이션된부분 아니면 정상 이진탐색
                high = mid-1;
            }else{
                low = mid+1;
            }
        }else{
            if(m < target && target <= nums[high]){
                low = mid+1;
            }else{
                high = mid-1;
            }
        }
    }
    return nums[low] === target? low : -1;
};


/*
    총 네가지 경우가 있다.
    먼저 타겟이 mid보다 작은지 큰지를 확인해보자.
    
    1. 타겟이 mid보다 작다?
    [5,6,7,0,1,2]
    => mid 가 7이라고 해봐. (타겟이 앞에 붙어있는지 뒤에있는지는 아직 모르는상태)
    우린 타겟이 7보다 작다는걸 알지만 왼쪽이나 오른쪽 둘다 mid보다 작기(타겟이 있을수있기)때문에
    어디로 가야할지 모름
    이러면 low(현재 범위 맨앞)랑 target을 비교해보자.
    타겟이 low보다 크다면 당연 앞쪽에 있는거고 low보다 작으면 뒤쪽에 있는거임
    ㄴ 아 근데 여기서 mid가 1이고 타겟이 0이면 타겟이 mid보다 작지만 target이 앞에있음
       이런 경우를 생각 못해서 계속 틀렸네 ㅠㅠ
       이것때문에 mid가 로테이션 된 부분인지 아닌지 확인해줘야함
       mid를 [low]랑 비교해줌. low보다 mid가 크다면 정방향이겠고 low>mid면 로테이션 된거
    
    
    2. 타겟이 mid보다 크다?
    [5,6,7,0,1,2]
    이번엔 mid가 0이야.
    이때 위에처럼 low랑 target을 비교하면 target이 있는 위치 정확히 알지 못함.
    앞으로가도 mid보다 클 수 있고 뒤로가도 클 수 있기때문.
    이 경우엔 high랑 비교해주자
    타겟이 high보다도 크다면 앞쪽에, high보다 작으면 뒤쪽에 있는거
    
    
    
    ====================================
    위에 틀려서 다시함
    먼저 mid가 로테이션 되어 뒤에 붙은 부분인지 확인해줘야함
    low랑 mid를 비교해서 mid가 더 작다면 이 mid는 로테이션된 부분임.
    
    1. 그럼 일단 mid가 로테이션 되지 않은 부분(=정상부분이라 하겠음)일때를 먼저 보자.
      low ~ mid 는 mid의 뒤에 정상 부분이 더 있건말건 어쨌든 이 부분은 정상부분임이 확실함
      그럼 target이 이 범위 안에 있다면 원래의 이진탐색 해주면됨
      그렇지 않은 경우는? 뒤를 새 범위로 잡아서 다음 루프로 돌려준다.
    
    2. mid가 로테이션된 부분일때
      이 경우는 mid의 뒤로는 전부 로테이션 부분임.
      그러니 타겟이 이 범위에 포함된다면 정상 이진탐색 해준다.
      그렇지 않은 경우는 앞을 새 범위로 잡아서 다음 루프 돌려줌
      
    *** 이거 할 때 등호 개중요함. 이거때문에 개 삽질 ㅅㅂ
    
*/
