class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        match = {}  # key는 s의 알파벳, value는 t 의 알파벳/ 이걸로 짝을 지을거임
        for ss, tt in zip(s, t):
            if ss in match:
                if match[ss] != tt:
                    return False
            else:
                if tt in match.values():
                    return False
                match[ss] = tt

        return True

    # https://leetcode.com/problems/word-pattern/ 와 매우 비슷
