---
date: '2022-05-25'
---

```python
class Solution:
    def smallestStringWithSwaps(self, s: str, pairs: List[List[int]]) -> str:
        def dfs(curr):
            if not visited[curr]:
                visited[curr] = True
                # 상위 스코프 paths에 추가. 아래에서 dfs돌리면 각 depth로 들어가게돼서 바깥에서 관리해야함
                paths.append(curr)
                for nexts in link[curr]:
                    dfs(nexts)
            return
        
        n = len(s)
        link = [[] for _ in range(n)]  # 인덱스를 키로해서 pairs에서 짝이되는 모든 값들 저장
        lists = list(s)
        visited = [False for _ in range(n)]
        for p in pairs:
            # 0번이랑 1번 중 어디가 다른 노드랑 연결될 지 모르기때문에 둘 다 저장
            link[p[0]].append(p[1])
            link[p[1]].append(p[0])
        
        for i in range(n):
            paths = []  # i랑 연결된 swap 할수있는 모든 인덱스 관리할곳
            dfs(i)
            
            chars = [lists[p] for p in paths]
            
            paths.sort()
            chars.sort()
            for k in range(len(paths)):
                lists[paths[k]] = chars[k]  # 정렬한 인덱스와 문자열을 다시 끼워넣음
            
        
        return ''.join(lists)
```

```javascript
/**
 * @param {string} s
 * @param {number[][]} pairs
 * @return {string}
 */
var smallestStringWithSwaps = function(s, pairs) {
    const dfs =(curr)=>{
        if(!visited[curr]){
            visited[curr] = true;
            paths.push(curr);
            
            for(const next of linked[curr]){
                dfs(next);
            }
        }
        return;
    }
    
    const n = s.length;
    const linked = Array.from(Array(n), () => []);
    const paths = [];
    const visited = new Array(n).fill(false);
    const list = s.split('');
    
    for(const p of pairs){
        linked[p[0]].push(p[1]);
        linked[p[1]].push(p[0]);
    }
    for(let i=0; i<n; i++){
        paths.splice(0);  // i마다 새로운 paths를 가져야 하기때문에 매번 초기화해줘야함
        dfs(i);
        
        const chars = [];  // paths에서 모은 인덱스들에서 거기에 해당하는 문자만 가져올거임
        for(const p of paths){
            chars.push(list[p]);
        }
        chars.sort();
        paths.sort((a,b)=>a-b);
        for(let x=0; x<paths.length; x++){
            list[paths[x]] = chars[x];  // 앞 인덱스부터 정렬된 알파벳 대체하기
        }
    }
    
    return list.join('');
};
```
