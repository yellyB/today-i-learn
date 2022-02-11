/**
 * Definition for isBadVersion()
 *
 * @param {integer} version number
 * @return {boolean} whether the version is bad
 * isBadVersion = function(version) {
 *     ...
 * };
 */

/**
 * @param {function} isBadVersion()
 * @return {function}
 */
var solution = function (isBadVersion) {
  /**
   * @param {integer} n Total versions
   * @return {integer} The first bad version
   */
  return function (n) {
    let start = 0;
    let end = n;

    while (start <= end) {
      const mid = Math.floor((start + end) / 2);
      if (isBadVersion(mid)) end = mid - 1;
      else start = mid + 1;
    }
    return start;
  };
};

/*
[이진 탐색]

1. 절반을 확인하고

1-1. 불량임? 걔가 첫 불량품인지 확인하기 위해 앞에꺼 검사. 1번으로 돌아감
1-2. 불량 아님? 그럼 그 뒤쪽에 있단 뜻이니 다음 절반을 검사 ㄱㄱ. 1번으로

*/
