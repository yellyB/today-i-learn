---
date: '2021-12-03'
---

```python
class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if digits == '': return []
        keyPad = ['','','abc','def', "ghi", "jkl", "mno", "pqrs", "tuv", "wxyz"]
        combinations = ['']
        for digit in digits:
            canPush = keyPad[int(digit)]
            temp = []
            for combination in combinations:
                # print(combination)
                for item in canPush:
                    # print(combination+item)
                    temp.append(combination+item)
            combinations = temp


        return combinations
```

```javascript
/**
 * @param {string} digits
 * @return {string[]}
 */
var letterCombinations = function(digits) {
    if(digits.length === 0) return [];
       
    const map = {
        2: ['a', 'b', 'c'],
        3: ['d', 'e', 'f'],
        4: ['g', 'h', 'i'],
        5: ['j', 'k', 'l'],
        6: ['m', 'n', 'o'],
        7: ['p', 'q', 'r', 's'],
        8: ['t', 'u', 'v'],
        9: ['w', 'x', 'y', 'z'],
    };
    
    const func=(idx, curr, res)=>{
        if(idx === digits.length){
            res.push(curr);
            return res;
        }
        for(const x of map[digits[idx]]){
            func(idx+1, curr+x, res);
        }
        return res
    }
    return func(0, '', []);
};
```
