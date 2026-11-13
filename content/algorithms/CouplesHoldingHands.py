class Solution:
    def minSwapsCouples(self, row: List[int]) -> int:
        # 내 짝의 조건:   1. 짝<홀, 2. 두개 1만 차이나야함
        def getPair(num):
            if num % 2 == 0:
                return num + 1
            else:
                return num - 1
        
        swap = 0
        for i in range(0, len(row), 2):
            pair = getPair(row[i])
            if pair != row[i+1]:  # 짝이 맞지 않다? 맞는애 찾아서 바꾸기
                for j in range(i+2, len(row)):
                    if row[j] == pair:
                        row[j] = row[i+1]  # i는 굳이 바꿀 필요 없으니 뒤에애만 바꿔주겠음
                        swap += 1
                        break
            
        return swap
