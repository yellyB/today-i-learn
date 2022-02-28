/**
 * @param {number[]} salary
 * @return {number}
 */
var average = function(salary) {
    let min = salary[0]
    let max = salary[0]
    let sum = 0
    for(const sal of salary){
        sum += sal
        if(sal < min) {
            min = sal
        }else if(sal > max){
            max = sal
        }
    }
    
    return (sum - min - max) / (salary.length - 2)
};
