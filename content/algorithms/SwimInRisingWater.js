/**
 * @param {number[][]} grid
 * @return {number}
 */
var swimInWater = function(grid) {
    const visited = new Set();
    let time = 0;
    let n = grid.length;
    
    // 각 칸마다 번호를 붙여서
    // 그 칸의 값이 적어도 time보다 작다면 수영가능
    // 값이 time보다 크다면 time을 1씩 늘려가면서 끝까지 갈 수 있을때까지 검사
    const dfs =(row, col)=>{
        if(0<=row && row<n && 0<=col && col<n && !visited.has(row*n+col) && grid[row][col] <= time){
            visited.add(row*n+col);
            for(const [r, c] of [[0,1],[1,0],[0,-1],[-1,0]]){
                dfs(row+r, col+c);
            }
        }
        return
    }
    
    while(!visited.has(n*n-1)){
        visited.clear();
        dfs(0,0);
        time ++;
    }
    
    return time-1;
};
