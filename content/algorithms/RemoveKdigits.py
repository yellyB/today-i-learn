class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        # k만큼 반복, num에서 현재 값이 뒤 값보다 크면 현재값 삭제
        # 삭제하고 나면 k줄이고 다시 num의 처음부터 검사
        while k > 0:
            i = 0
            # for문 쓰는 경우에 num길이가 1이면 아예 안돌고 넘어가는데
            # 이럴경우 i가 선언되지 못해서 에러남
            while i < len(num) - 1:
                if num[i] > num[i + 1]:
                    break
                i += 1
            num = num[:i] + num[i + 1:]
            k -= 1

        if num == "": return "0"
        return str(int(num))