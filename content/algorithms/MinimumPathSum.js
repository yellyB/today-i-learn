/**
 * @param {number[][]} grid
 * @return {number}
 */
var minPathSum = function(grid) {
    for (let i in grid){
        for (let j in grid[0]){
            if (i == 0 && j != 0){
                grid[0][j] += grid[0][j-1]
            }else if(i != 0 && j == 0){
                grid[i][0] += grid[i-1][0]
            }else if(i != 0 && j != 0){
                grid[i][j] += Math.min(grid[i-1][j], grid[i][j-1])
            }
        }
    }
    return grid[grid.length-1][grid[0].length-1]

};