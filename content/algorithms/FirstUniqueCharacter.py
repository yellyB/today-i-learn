class Solution:
    def firstUniqChar(self, s: str) -> int:
        for i in range(len(s)):
            isSame = False  # 같은게 존재하는지? 초기값은 false
            for j in range(len(s)):
                # 자기자신 아닌것중 같은거 있음 isSame=True하고 종료
                if i != j and s[i] == s[j]:
                    isSame = True
                    break
            # 다 돌았는데 같은게 없었다면 인덱스 반환
            if isSame == False:
                return i
        # 아무것도 없었다면 -1 반환
        return -1