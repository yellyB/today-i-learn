class Solution:
    def countOdds(self, low: int, high: int) -> int:
        answer = 0
        if low % 2 != 0 and high % 2 != 0: answer += 1
        return answer + ceil((high - low) / 2)
    
    # low 랑 high 의 차이에 /2를 하면 홀수 갯수 알 수 있는데
    # low랑 high가 둘 다 홀수면 위에서 구한 갯수 +1 해줘야함
