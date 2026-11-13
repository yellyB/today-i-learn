class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        dic = {}

        def getPalCnt(start, end):
            if (start, end) in dic: return dic[(start, end)]  # 이미 계산했었으면 리턴

            if start > end: return 0
            if start == end: return 1

            if s[start] == s[end]:  # 같은거 찾았으면 계속 돌림
                dic[(start, end)] = getPalCnt(start + 1, end - 1) + 2  # 시작위치랑 끝위치 2개 더해줌
                return dic[(start, end)]

            # start만 증가 & end만 감소 -> 둘 경우 각각 비교
            dic[(start + 1, end)] = getPalCnt(start + 1, end)
            dic[(start, end - 1)] = getPalCnt(start, end - 1)

            return max(dic[(start + 1, end)], dic[(start, end - 1)])

        return getPalCnt(0, len(s) - 1)

# 5. Longest Palindromic Substring 이거 업글 문제임

