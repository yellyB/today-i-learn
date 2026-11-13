/**
 * @param {character[][]} grid
 * @return {number}
 */
var numIslands = function(grid) {
    const rowLen = grid.length;
    const colLen = grid[0].length;
    let cnt = 0;
    const getCount = (i, j) => {
        if(i < 0 || j < 0 || i >= rowLen || j >= colLen) return
        if(grid[i][j] == '1'){
            grid[i][j] = '0';
            getCount(i, j+1);
            getCount(i, j-1);
            getCount(i+1, j);
            getCount(i-1, j);
            
        }
    }
    
    for(let i=0; i<rowLen; i++){
        for(let j=0; j<colLen; j++){
            if(grid[i][j] == '1'){
                getCount(i, j);
                cnt ++;
            }
            
        }
    }
    
    
    return cnt
};
