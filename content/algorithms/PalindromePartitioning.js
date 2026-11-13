/**
 * @param {string} s
 * @return {string[][]}
 */
var partition = function(s) {
  const isPalindrome = (str) => {
    let start = 0;
    let end = str.length - 1;
    while (start <= end) {
      if (str[start] !== str[end]) return false;
      start++;
      end--;
    }
    return true;
  };

  const partitioning = (prev, str) => {
    if (str.length === 1) return;
    for (let i = 0; i < str.length-1; i++) {
      const front = str.slice(0, i + 1);
      const back = str.slice(i + 1);
      if (isPalindrome(front)) {
        if (isPalindrome(back)) {
          answer.push([...prev,front,back]);
        }
        partitioning([...prev, front], back);
      }
    }
  };

  const answer = [];
  partitioning([], s);
    
  if(isPalindrome(s)) answer.push([s]);

  return answer;
};
