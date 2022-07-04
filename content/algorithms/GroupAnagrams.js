/**
 * @param {string[]} strs
 * @return {string[][]}
 */
var groupAnagrams = function(strs) {
    const map = {};
    
    for(const s of strs){
        const sortedStr = [...s].sort();
        map[sortedStr] = map[sortedStr] ? [...map[sortedStr], s] : [s];
    }
    
    return Object.values(map);  // 객체의 값만 뽑기
};
