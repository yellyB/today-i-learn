class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        checked = []
        for r in ransomNote:
            if r not in checked and ransomNote.count(r) > magazine.count(r):
                return False
            else:
                checked.append(r)
        return True

    # ransomNote의 알파벳이 magazine에 없거나 숫자가 더 적으면 false임.
    # 그니까 둘한테서 알파벳 갯수 세서 비교하면 됨
    # 이미 체크한거는 또 할 필요 없음