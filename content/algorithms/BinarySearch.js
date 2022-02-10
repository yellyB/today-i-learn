/**
 * @param {number[]} nums
 * @param {number} target
 * @return {number}
 */
var search = function (nums, target) {
  let start = 0;
  let end = nums.length - 1;

  while (start <= end) {
    const mid = Math.round((start + end) / 2);
    if (nums[mid] == target) {
      return mid;
    } else if (nums[mid] < target) {
      start = mid + 1;
    } else {
      end = mid - 1;
    }
  }
  return -1;
};

/*

[이진 탐색]
nums가 오름차순으로 주어지기 때문에 이진탐색 알고리즘 사용할 수 있음
왼, 오를 중간값으로 대체하면서 원하는 타겟넘버를 찾아나간다.

*/
