from functools import lru_cache

class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        @lru_cache(None)  # 결과 캐싱
        def isInDict(start):
            # 4. 3번에서 재귀돌렸을때 현재문자열위치+1을 보내니까
            # 그걸 시작위치로 받았을 때 그게 전체 문자열길이와 같다면 끝까지 돌때까지 False로 안떨어진것
            if start == len(s): return True

            # 2. 받은 시작위치부터 문자열의 끝까지 검사함
            for end in range(start, len(s)):
                word = s[start:end + 1]
                # 3. 문자열이 사전에 있다면
                if word in wordDict:
                    res = isInDict(end + 1)
                    # 3-1. 그 이후의 문자열도 검사해서 다 있는 단어라면 True
                    if res:
                        return True
                    # 3-2. 그 이후의 문자열중 사전에 없는애가 있다면 False
                    else:
                        continue

            return False

        return isInDict(0)  # 1. 시작 위치를 넘김