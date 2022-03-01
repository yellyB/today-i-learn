/**
 * @param {number} n
 * @return {number}
 */
var subtractProductAndSum = function(n) {
    let sum = 0;
    let mul = 1;
    while(n > 0){
        sum += n % 10;
        mul *= n % 10;
        n = Math.floor(n/10);
    }
    return mul - sum
};
