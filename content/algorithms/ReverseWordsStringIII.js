/**
 * @param {string} s
 * @return {string}
 */
var reverseWords = function (s) {
  let answer = "";
  let word = "";

  for (const w of s) {
    if (w !== " ") {
      word = w + word;
    } else {
      answer += word + w;
      word = "";
    }
  }

  return answer + word;
};
