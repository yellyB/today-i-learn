---
date: '2022-05-14'
---

```python
class Solution:
    def queensAttacktheKing(self, queens: List[List[int]], king: List[int]) -> List[List[int]]:
        res = []
        def bfs(king, dx, dy):
            if 0<=king[0]<8 and 0<=king[1]<8:
                if king in queens:
                    res.append(king)
                else:
                    bfs([king[0]+dx,king[1]+dy], dx, dy)
        
        # 위부터 시계방향으로 검사
        bfs(king[:], -1, 0)
        bfs(king[:], -1, 1)
        bfs(king[:], 0, 1)
        bfs(king[:], 1, 1)
        bfs(king[:], 1, 0)
        bfs(king[:], 1, -1)
        bfs(king[:], 0, -1)
        bfs(king[:], -1, -1)
        
        return res
```

```javascript
/**
 * @param {number[][]} queens
 * @param {number[]} king
 * @return {number[][]}
 */
var queensAttacktheKing = function(queens, king) {
    const res = [];
    
    const bfs = (king, dx, dy) =>{
        if(king[0]<0 || king[0]>=8 || king[1]<0 || king[1]>=8) return;
        if(dx==0 && dy==0) return;
        // 이중배열인 queens에서 배열인 king을 찾는거라 indexOf나 includes로는 검사 불가
        if(queens.find((queen)=> queen[0] == king[0] && queen[1] == king[1])){
            res.push(king);
        }
        else{
            bfs([king[0]+dx, king[1]+dy], dx, dy)
        }
        return;
    }
    
    // 팔방 다 검사
    for(const i of [-1,0,1]){
        for(const j of [-1,0,1]){
            bfs([king[0]+i, king[1]+j], i, j);
        }
    }
    
    
    return res
    
};
```
