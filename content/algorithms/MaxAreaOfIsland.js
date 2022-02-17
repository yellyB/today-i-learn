/**
 * @param {number[][]} grid
 * @return {number}
 */
var maxAreaOfIsland = function (grid) {
  const rowLen = grid.length;
  const colLen = grid[0].length;
  let maxCnt = 0;

  const counting = (row, col) => {
    let cnt = 0;
    if (
      row === -1 ||
      col === -1 ||
      row === grid.length ||
      col === grid[0].length ||
      grid[row][col] === 0
    )
      return 0;
    grid[row][col] = 0;
    cnt++;

    cnt +=
      counting(row - 1, col) +
      counting(row, col + 1) +
      counting(row + 1, col) +
      counting(row, col - 1);

    return cnt;
  };

  for (let row = 0; row < rowLen; row++) {
    for (let col = 0; col < colLen; col++) {
      if (grid[row][col] === 1) {
        const cnt = counting(row, col);
        maxCnt = cnt > maxCnt ? cnt : maxCnt;
      }
    }
  }
  return maxCnt;
};
