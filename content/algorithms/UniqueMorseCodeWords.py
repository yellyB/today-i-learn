class Solution:
    def uniqueMorseRepresentations(self, words: List[str]) -> int:
        # 이중 for문으로 글자 하나에 대응하는 모스 부호를 찾아서 합침(단어를=>모스부호)
        # 바꾼걸 morses에 넣고 이미 있으면 cnt 1씩 증가
        cnt = 0
        morse = [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
        morses = []
        print(ord('a'))  # 97
        print(ord('z'))  # 122
        for word in words:
            wordToMorse = ''
            for letter in word:
                ascCode = morse[ord(letter)-97]
                wordToMorse += ascCode
            if wordToMorse not in morses:
                morses.append(wordToMorse)
                cnt += 1
        return cnt