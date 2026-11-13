---
date: '2022-05-24'
---

```python
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # cycle이 있으면 무조건 F이다.
        # cycle이 하나라도 있는지 확인해야함
        
        
        def dfs(key, visited):
            if key in visited: return False  # 확인중인 목록에 있으면 cycle일수밖에
            if key in checked: return True  # 완전 확인끝난 애들에 포함되어있다면 얜 안전. 확인할필요 X
            
            if key in pre:
                for val in pre[key]:
                    if not dfs(val, visited+[key]): return False
                    
            checked.append(key)  # 위 for문에서 중단당하지 않았다면 얜 안전!
            return True
        
        
        pre = {}  # 딕셔너리로 짝지을거. key를 얻으려면 [val]에 있는애들 먼저해야함
        checked = []  # 전부 다 봐서 cycle없는거 확인 끝마친 애들
        
        for p in prerequisites:
            if p[0] in pre: pre[p[0]].append(p[1])
            else: pre[p[0]] = [p[1]]
                
        
        # numCourses-1 까지 전부 통과해야 최종적으로 T를 리턴할 수 있음. 그러니 하나씩 다 검사
        for i in range(numCourses):
            if not dfs(i, []): return False  # 하나라도 F면 즉시 리턴
        
        return True
```

```javascript
/**
 * @param {number} numCourses
 * @param {number[][]} prerequisites
 * @return {boolean}
 */
var canFinish = function(numCourses, prerequisites) {
    const bfs=(key, visited)=>{
        if(visited.includes(key)) return false;  // 지금 검사중인 목록에 있으면 cycle임.
        if(checked.includes(key)) return true;  // 검사 끝난 목록에 있으면 어차피 true임
        
        // key에 해당하는 값 다 확인해서
        // 하나라도 f 면 바로 리턴
        if(map.get(key)!==undefined){
            for(const val of [...map.get(key)]){
                if(!bfs(val, [...visited, key])) return false;
            }
        }
        
        // 위 단계 전부 통과했으면 얘(key)는 안전한애
        checked.push(key);
        return true;
    }
    
    const checked = [];  // 완벽히 끝까지 체크한 애들
    const map = new Map();  // [0]을 하기위해 [1]에있는 배열을 다 만족해야 함. 이걸 여기에 정리할거임
    
    for(const p of prerequisites){
        // map.set(p[0], map.get(p[0]) ? [map.get(p[0])]+[p[1]] : p[1] );
        if(map.has(p[0])){
            map.set(p[0], [...map.get(p[0]), p[1]]);
        }else{
            map.set(p[0], [p[1]]);
        }
    }
    
    // numCourses-1 만큼은 다 검사해서, 하나라도 F면 안됨
    for(let i=0; i<numCourses; i++){
        if(!bfs(i, [])) return false;
    }
    
    
    return true;
};
```
