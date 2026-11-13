/**
 * @param {character[][]} board
 * @param {string} word
 * @return {boolean}
 */
var exist = function(board, word) {
    const checkWord=(i, j, word)=>{
        if(word.length == 0) {console.log(i, j,word, word.length);return true;}
        if(i<0 || i>=board.length || j<0 || j>=board[0].length || word[0]!==board[i][j]) return false;
        
        board[i][j] = '.';  // visited 처리
        if(checkWord(i, j+1, word.slice(1)) || checkWord(i+1, j, word.slice(1)) || checkWord(i, j-1, word.slice(1)) || checkWord(i-1, j, word.slice(1))){
            return true;
        }
        board[i][j] = word[0];
        
        return false;
    }
    
    
    for(let i=0; i<board.length; i++){
        for(let j=0; j<board[0].length; j++){
            if(checkWord(i, j, word)){
                return true;
            }
        }
    }
    
    return false;
};
