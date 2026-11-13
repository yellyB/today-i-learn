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
