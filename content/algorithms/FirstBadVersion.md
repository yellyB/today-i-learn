---
date: '2021-11-08'
---

```python
# The isBadVersion API is already defined for you.
# @param version, an integer
# @return an integer
# def isBadVersion(version):

class Solution:
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        left = 1
        right = n - 1
        while left <= right:
            mid = left + (right - left) // 2  # 앞에 left를 더하는건 그래야 절반의 절반 갈때 그 위치로 가기 가능
            if isBadVersion(mid):
                right = mid - 1  # 이보다 앞에 bad가 있을 수 있으니 ㄱㄱ
            else:
                left = mid + 1

        return left

    # binary Search 이용. 절반 확인해서 걔보다 큰지 작은지. 그래서 절반을 다시 갱신. 이걸 찾을때까지
```

```javascript
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
```
