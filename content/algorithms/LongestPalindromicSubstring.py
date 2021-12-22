class Solution:
    def longestPalindrome(self, s: str) -> str:
        length = len(s)
        sIdx = 0
        eIdx = 0

        def isPal(start, end):
            if start > 0 and end < length - 1:  # start랑 end가 한칸씩 이동할 곳이 있는 경우만 실행
                if s[start - 1] == s[end + 1]:
                    start -= 1
                    end += 1
                    return isPal(start, end)
            return start, end

        for i in range(len(s) - 1):
            odd = isPal(i, i)  # 자기 자신과 비교
            even = isPal(i + 1, i)  # 자기랑 자기뒤랑 비교
            oddS, oddE = odd[0], odd[1]
            evenS, evenE = even[0], even[1]

            if oddE - oddS > eIdx - sIdx:
                sIdx, eIdx = oddS, oddE
            if evenE - evenS > eIdx - sIdx:
                sIdx, eIdx = evenS, evenE

        return s[sIdx:eIdx + 1]
