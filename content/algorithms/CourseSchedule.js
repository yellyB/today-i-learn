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
