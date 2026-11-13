---
date: '2021-06-19'
---

```python
class Solution:
    def maxSatisfaction(self, satisfaction: List[int]) -> int:
        # 5,3,0,-1,-2,-3 일 때
        # 처음에는 total = 5*1
        # 그 다음으로 큰 수는 3인데 3이 0번에 추가되면
        # 5의 계수는 2가 되고 3은 새로 1로 추가되니까
        # total = (5*1) 에 (3*1)+(5*1)이 됨  //(3*1)->추가된거 (5*1)->한칸씩 밀릴거
        # 계수의 리스트가 늘어날 때마다
        # 이전 총 합 + 새로 0번 인덱스에 추가될 값 + 한칸씩 뒤로 밀릴 숫자들 합계(계수1씩만)
        # 방금 추가된 값은 다음번 한칸씩 밀릴 합계(tempTotal)에 포함시켜야함
        result = []  #합계 결과들 저장
        total = 0  #전체 총 합
        tempTotal = 0  #한 칸 밀릴 숫자들 합
        satisfaction.sort(reverse=True)
        if satisfaction[0] < 0:
            return 0
        for num in satisfaction:
            tempTotal = tempTotal + num
            if total==0:
                total = num
            else:
                total = total + tempTotal
                result.append(total)
        return max(result)
```

```javascript
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
```
