/**
 * @param {string} s
 * @return {number}
 */
var lengthOfLongestSubstring = function (s) {
  let max = 0;
  let l = 0;
  for (let r = 0; r < s.length; r++) {
    const idx = s.slice(l, r).indexOf(s[r]);
    if (idx === -1) {
      max = Math.max(max, r + 1 - l);
    } else {
      l += idx + 1;
    }
  }
  return max;
};
