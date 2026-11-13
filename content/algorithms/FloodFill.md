---
date: '2021-08-03'
---

```python
class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:
        def changeValue(sr, sc):
            if 0 <= sr < len(image) and 0 <= sc < len(image[0]):
                if image[sr][sc] == flood:
                    image[sr][sc] = newColor
                    changeValue(sr + 1, sc)
                    changeValue(sr - 1, sc)
                    changeValue(sr, sc + 1)
                    changeValue(sr, sc - 1)

        flood = image[sr][sc]  # 맨 처음 타겟된 숫자, 앞으로 이 숫자랑 같으면 바꿔줄거임
        if flood == newColor:
            return image

        changeValue(sr, sc)

        return image
```

```javascript
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

  if (newColor === num) return image; // 바꿀값이 없으면 그대로 리턴

  changeVal(sr, sc);

  return image;
};
```
