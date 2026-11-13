/**
 * @param {number[][]} mat
 * @param {number} r
 * @param {number} c
 * @return {number[][]}
 */
var matrixReshape = function(mat, r, c) {
    let rowLen = mat.length
    let colLen = mat[0].length
    
    if(r*c !== rowLen*colLen){
       return mat;
       }
    
    let row = 0;  // 새로 만들 array의 row
    let col = 0;
    const arr = Array.from(Array(r), () => Array(c));  // 2차원 배열 만들고
    
    
    // 새로만들 arr의 포인터를 각각 지정해서
    // col을 하나씩 증가시킨다. col이 목표colLen인 c에 도달하면 row를 하나 증가, col은 초기화
    for(let i=0; i<mat.length; i++){
        for(let j=0; j<mat[0].length; j++){
            arr[row][col] = mat[i][j];
            col ++;
            if(col>=c) {
                row ++;
                col = 0;
            }
        }
    }
    
    return arr
};
