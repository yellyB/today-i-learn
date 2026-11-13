/**
 * @param {string} s1
 * @param {string} s2
 * @return {boolean}
 */
var checkInclusion = function (s1, s2) {
  const len = s1.length;
  const arr1 = Array(26).fill(0);
  const arr2 = Array(26).fill(0);

  for (const s of s1) {
    const idx = s.charCodeAt() - 97;
    arr1[idx] += 1;
  }

  for (const i in s2) {
    const s = s2[i];
    const idx = s.charCodeAt() - 97;
    arr2[idx] += 1;

    if (i >= len) arr2[s2[i - len].charCodeAt() - 97] -= 1;
    if (arr1.toString() == arr2.toString()) return true;
  }
  return false;
};
