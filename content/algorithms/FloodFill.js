/**
 * @param {number[][]} image
 * @param {number} sr
 * @param {number} sc
 * @param {number} newColor
 * @return {number[][]}
 */
var floodFill = function (image, sr, sc, newColor) {
  const num = image[sr][sc]; // 기준 숫자. 이거랑 같으면 바꿔줄거
  const rowLen = image.length;
  const colLen = image[0].length;

  const changeVal = (i, j) => {
    if (i === -1 || i === rowLen) return;
    if (j === -1 || j === colLen) return;
    if (image[i][j] !== num) return;

    image[i][j] = newColor;

    changeVal(i - 1, j); //위
    changeVal(i, j + 1); //오
    changeVal(i + 1, j); // 밑
    changeVal(i, j - 1); // 왼
  };

  if (newColor === num) return image;

  changeVal(sr, sc);

  return image;
};

console.log(
  floodFill(
    [
      [0, 0, 0],
      [0, 1, 1],
    ],
    1,
    1,
    1
  )
);
