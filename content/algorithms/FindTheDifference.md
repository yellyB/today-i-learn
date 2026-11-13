---
date: '2022-03-09'
---

```python
class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        # 아스키 코드 이용
        ascS = 0
        ascT = ord(t[-1])
        for i in range(len(s)):
            ascS += ord(s[i])
            ascT += ord(t[i])
        return chr(ascT - ascS)
```

```javascript
/**
 * @param {string} s
 * @param {string} t
 * @return {character}
 */
var findTheDifference = function(s, t) {
    let ascS = 0;
    let ascT = t.charCodeAt(t.length-1);
    for(let i=0; i<s.length; i++){
        ascS += s.charCodeAt(i);
        ascT += t.charCodeAt(i);
    }
    return String.fromCharCode(ascT - ascS);
};
```
