/**
 * @param {number[][]} matrix
 */
var NumMatrix = function(matrix) {
    const r = matrix.length;
    const c = matrix[0].length;
    const dp = Array(r+1).fill(0).map(()=>Array(c+1).fill(0));
    for(let i=1; i<=r; i++){
        for(let j=1; j<=c; j++){
            dp[i][j] = dp[i][j-1] + dp[i-1][j] + matrix[i-1][j-1] - dp[i-1][j-1];  // 누적 합계
        }
    }
    this.dp = dp;
};

/** 
 * @param {number} row1 
 * @param {number} col1 
 * @param {number} row2 
 * @param {number} col2
 * @return {number}
 */
NumMatrix.prototype.sumRegion = function(row1, col1, row2, col2) {
    // dp에서 [0]젤 왼, 젤 위 계산을 위해 비워뒀어서 인덱스가 하나씩 밀려있는 상태. 그래서 +1해줘서 계산
    row1++; col1++; row2++; col2++;
    
    return this.dp[row2][col2] - this.dp[row2][col1-1] - this.dp[row1-1][col2] + this.dp[row1-1][col1-1];
};

/** 
 * Your NumMatrix object will be instantiated and called as such:
 * var obj = new NumMatrix(matrix)
 * var param_1 = obj.sumRegion(row1,col1,row2,col2)
 */
