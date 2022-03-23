/**
 * @param {number[][]} mat
 * @return {number[][]}
 */
var diagonalSort = function(mat) {
    const sorting=(row, col)=>{
        const temp = [];
        while(row<rowLen && col<colLen){
            temp.push(mat[row][col]);
            row ++;
            col ++;
        }
        temp.sort((a,b)=> a-b);
        while(row>0 && col>0){
            row --;
            col --;
            mat[row][col] = temp.pop();
        }
        
        return
    }
    const rowLen = mat.length;
    const colLen = mat[0].length;
    
    for(let i=0;i<rowLen;i++) sorting(i, 0);  // 각 row에서 시작하는 대각선
    for(let j=0;j<colLen;j++) sorting(0, j);  // [0] row의 col에서 시작하는 대각선
    
    return mat
};
