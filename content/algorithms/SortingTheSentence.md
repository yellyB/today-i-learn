---
date: '2022-04-27'
---

```python
class Solution:
    def sortSentence(self, s: str) -> str:
        answer = ''
        splited = s.split()
        arr = []  # [번호:문자열] 형태로 이중배열로 저장
        for sp in splited:
            arr.append([sp[-1:], sp[:-1]])
            
        arr.sort()
        
        return ' '.join([i[1] for i in arr])
```

```javascript
/**
 * @param {string} s
 * @return {string}
 */
var sortSentence = function(s) {
    return s.split(' ').sort((a, b)=>a[a.length-1]-b[b.length-1]).map((item)=>item.slice(0,item.length-1)).join(' ');
};
```
