/**
 * @param {string} digits
 * @return {string[]}
 */
var letterCombinations = function(digits) {
    if(digits.length === 0) return [];
       
    const map = {
        2: ['a', 'b', 'c'],
        3: ['d', 'e', 'f'],
        4: ['g', 'h', 'i'],
        5: ['j', 'k', 'l'],
        6: ['m', 'n', 'o'],
        7: ['p', 'q', 'r', 's'],
        8: ['t', 'u', 'v'],
        9: ['w', 'x', 'y', 'z'],
    };
    
    const func=(idx, curr, res)=>{
        if(idx === digits.length){
            res.push(curr);
            return res;
        }
        for(const x of map[digits[idx]]){
            func(idx+1, curr+x, res);
        }
        return res
    }
    return func(0, '', []);
};
