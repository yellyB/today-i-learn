class Solution:
    def cellsInRange(self, s: str) -> List[str]:
        return [chr(i) + str(j) for i in range(ord(s[0]), ord(s[3])+1) for j in range(int(s[1]), int(s[4])+1)]
    
    
        # res = []
        # for i in range(ord(s[0]), ord(s[3])+1):  # 문자열의 아스키코드 이용
        #     for j in range(int(s[1]), int(s[4])+1):  # 숫자 범위를 돌림
        #         res.append(chr(i) + str(j))
        # return res
