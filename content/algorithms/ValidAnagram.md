---
date: '2021-11-16'
---

```python
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t): return False
        sList = [0] * 26
        tList = [0] * 26
        for i in range(len(s)):
            sList[ord(s[i]) - 97] += 1
            tList[ord(t[i]) - 97] += 1

        return sList == tList

        # 567. Permutation in String 이랑 비슷하게 품
        # 알파벳 총 개수 26개 만큼의 빈 배열 두개 만듬
        # s랑 t검사해서 알파벳 빈도 수를 각각 저장
        # 두 리스트가 다르다면 false
```

```javascript
/**
 * @param {string} s
 * @param {string} t
 * @return {boolean}
 */
var isAnagram = function(s, t) {
    if (s.length !== t.length) return false;
    
    const sList = Array(26).fill(0);
    const tList = Array(26).fill(0);
    
    for(let i=0; i<s.length; i++){
        sList[s.charCodeAt(i) - 97] += 1;
        tList[t.charCodeAt(i) - 97] += 1;
    }
    
    return sList.join('') === tList.join('')
    
};
```
