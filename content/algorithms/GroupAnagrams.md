---
date: '2022-03-13'
---

```python
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        answer = []
        dic = {}
        for s in strs:
            sort = ''.join(sorted(s))
            if sort not in dic:
                dic[sort] = len(dic)
                answer.append([])
            answer[dic[sort]].append(s)
        return answer
```

```javascript
/**
 * @param {string[]} strs
 * @return {string[][]}
 */
var groupAnagrams = function(strs) {
    const map = {};
    
    for(const s of strs){
        const sortedStr = [...s].sort();
        map[sortedStr] = map[sortedStr] ? [...map[sortedStr], s] : [s];
    }
    
    return Object.values(map);  // 객체의 값만 뽑기
};
```
