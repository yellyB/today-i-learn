class Solution:
    def longestStrChain(self, words: List[str]) -> int:
        strDict = {}  # str : wordChain몇개?
        for str in words:
            strDict[str] = 1  # 초기값 전부 1
        for str in sorted(words, key=len):  # 정렬된 리스트 반복
            for i in range(len(str)):
                prevStr = str[:i]+str[i+1:]  # 알파벳 하나씩 제거
                if prevStr in strDict:  # 알파벳 하나 제거한게 dict에 있으면
                    strDict[str] = max(strDict[prevStr]+1, strDict[str])
        return max(strDict.values())