/**
 * @param {number[]} nums
 * @param {number} target
 * @return {number}
 */
var searchInsert = function (nums, target) {
  let start = 0;
  let end = nums.length;

  while (start < end) {
    const mid = Math.floor((start + end) / 2);
    if (nums[mid] == target) {
      return mid;
    } else if (nums[mid] < target) {
      start = mid + 1;
    } else {
      end = mid;
    }
  }
  return end;
};

/*

[이진 탐색]
중간 값을 구해서 target이 들어갈 위치를 검사함.
들어갈 위치를 못찾은 채 while문이 종료되었다면 가장 마지막에 들어가야 한다는 뜻

*/
