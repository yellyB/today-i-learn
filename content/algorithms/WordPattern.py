class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        splitToSpace = s.split(' ')  # 단어를 쪼개서 리스트에
        hash = {}  # key:value로 'a':'dog' 같이 저장
        if len(splitToSpace) != len(pattern):  # "aaa" "a a a a" 의 경우 대비
            return False
        for i, pat in enumerate(pattern):
            if pat in hash:  # key에 이미 저장된 값 있?
                if hash[pat] != splitToSpace[i]:
                    return False
            else:  # 없으면 key:value저장
                if splitToSpace[i] in hash.values():  # value에도 'dog'가 없나 확인
                    return False  # 이미 value에 저장돼있음 거짓
                hash[pat] = splitToSpace[i]
        return True