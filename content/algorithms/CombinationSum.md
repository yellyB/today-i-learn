---
date: '2021-07-12'
---

```python
class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        # target에서 선택한 숫자를 빼줌. 남은 숫자를 candidates로 만들 수 있는지 확인해야함
        # dp함수를 만들어서 restNum이랑(얘가 새로운 target임) 현재까지 선택된 candidate를 보냄
        # dp함수에서 restNum이 0이 되었다면 이때까지 선택한 num들을 answer에 추가시켜줘야함
        # restNum이 0보다 크면 계속 돌림 / 0보다 작으면 target을 넘겼단 뜻이니 그냥 return
        answer = []
        def dp(nums, target):
            for n in candidates:
                temp = nums[:]
                rest = target - n
                if rest > 0:
                    temp.append(n)
                    dp(temp, rest)
                elif rest == 0:
                    temp.append(n)
                    temp.sort()
                    if temp not in answer:  # 중복 제거를 위해 정렬해서 그게 이미 없는지?
                        answer.append(temp)

        dp([], target)

        return answer
```

```javascript
/**
 * @param {number[]} candidates
 * @param {number} target
 * @return {number[][]}
 */
var combinationSum = function(candidates, target) {
    const func=(sums, idx, curr, res)=>{
        if(idx == candidates.length) return res;
        for(let i=idx; i<candidates.length; i++){
            const tempSum = sums+candidates[i]
            if(tempSum == target){
                res.push([...curr, candidates[i]]);
            }else if(tempSum < target){
                func(tempSum, i, [...curr, candidates[i]], res)
            }
        }
        return res
        
    }
    return func(0, 0, [], [])  // (지금까지 합계, 현재 인덱스, 현재까지 선택 목록, 최종정답)
};
```
