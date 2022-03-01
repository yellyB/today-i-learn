/**
 * @param {number[][]} matrix
 * @param {number} target
 * @return {boolean}
 */
var searchMatrix = function(matrix, target) {
    const rowLen = matrix.length;
    const colLen = matrix[0].length;
    let s = 0;
    let e = rowLen * colLen;
    while (s < e){
        const mid = Math.floor((s+e)/2);
        const midVal = matrix[Math.floor(mid/colLen)][mid%colLen]
        if(midVal == target) return true
        else if(midVal < target) s = mid+1
        else e = mid-1
    }
    return false
};
