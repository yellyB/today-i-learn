class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        prefix=''
        minLen=min ([len (i) for i in strs])  # 요소 중 최소 길이
        one = strs.pop()  # 기준
        for i in range(minLen):
            for str in strs:
                if one[i]!=str[i]:
                    return prefix
            prefix += one[i]
        return prefix