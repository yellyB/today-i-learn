/**
 * @param {string} s
 * @param {string} t
 * @return {boolean}
 */
var isAnagram = function(s, t) {
    if (s.length !== t.length) return false;
    
    const sList = Array(26).fill(0);
    const tList = Array(26).fill(0);
    
    for(let i=0; i<s.length; i++){
        sList[s.charCodeAt(i) - 97] += 1;
        tList[t.charCodeAt(i) - 97] += 1;
    }
    
    return sList.join('') === tList.join('')
    
};
