/**
 * @param {string} beginWord
 * @param {string} endWord
 * @param {string[]} wordList
 * @return {number}
 */
var ladderLength = function(beginWord, endWord, wordList) {
    const wordDict = new Map();
    const len = beginWord.length;
    for(const word of wordList){
        for(let i=0;i<len;i++){
            const stared = word.slice(0, i) + '*' + word.slice(i+1, len);
            if(wordDict.has(stared)) wordDict.set(stared, [...wordDict.get(stared), word]);
            else wordDict.set(stared, [word]);
        }
    }
    const queue = [[beginWord, 1]];
    const visited = new Set();
    visited.add(beginWord);
    
    while(queue.length > 0){
        const [currWord, level] = queue.shift();
        for(let i=0; i<len; i++){
            const stared = currWord.slice(0, i) + '*' + currWord.slice(i+1, len);
            if(wordDict.has(stared)){
                for(const word of wordDict.get(stared)){
                    if(word == endWord) return level + 1;
                    if(!visited.has(word)){
                        visited.add(word);
                        queue.push([word, level+1]);
                    }
                }
            }
        }
    }
    return 0;
    
    
};
