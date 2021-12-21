class Solution:
    # op1 - 두 문자 길이 같아야함, 종류 같아야함
    # op2 - 각 그룹으로 묶은 갯수가 같아야함
    # 위 세가지 항목에 만족하지 않으면 False
    def closeStrings(self, word1: str, word2: str) -> bool:
        dictOne = {}
        dictTwo = {}

        if len(word1) != len(word2):
            return False

        for word in word1:
            if word not in dictOne:
                dictOne[word] = 1
            else:
                dictOne[word] += 1

        for word in word2:
            if word not in dictTwo:
                dictTwo[word] = 1
            else:
                dictTwo[word] += 1

        keysOne = sorted(list(dictOne.keys()))
        keysTwo = sorted(list(dictTwo.keys()))
        valsOne = sorted(list(dictOne.values()))
        valsTwo = sorted(list(dictTwo.values()))

        if keysOne != keysTwo:
            return False
        if valsOne != valsTwo:
            return False

        return True