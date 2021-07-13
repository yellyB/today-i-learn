class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        def gcd(str1, str2):
            # str1에 더 긴거 저장
            if len(str1) < len(str2):
                str1, str2 = str2, str1

            if str2 in str1[:len(str2)]:  # 그냥 str2 in str1 했다가 에러남 (AABB,AB가 들어올 경우 대비)
                str1 = str1.replace(str2, '')
                if str1 == '':
                    return str2
                else:
                    return gcd(str1, str2)
            else:
                return ''

        return gcd(str1, str2)