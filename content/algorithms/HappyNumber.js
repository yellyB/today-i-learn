/**
 * @param {number} n
 * @return {boolean}
 */
var isHappy = function(n) {
  const getNextNum = (n) => {
      let sum = 0
      while(n){
          sum += Math.pow(n%10,2)
          n = Math.floor(n/10)
      }
      return sum
  }
  
  let nextNum = getNextNum(n)
  
  while(n !== nextNum){
      n = getNextNum(n)
      nextNum = getNextNum(getNextNum(nextNum))
  }
  
  return n === 1
};
