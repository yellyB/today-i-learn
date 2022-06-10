class Solution:
    def minOperations(self, boxes: str) -> List[int]:
        n = len(boxes)
        answer = [0] * n
        f, b = 0, 0   # 각 단계의 누적
        f_total, b_total = 0, 0  # 전체 단계 누적
        for i in range(n):
            answer[i] += f_total
            answer[n-1-i] += b_total
            f += int(boxes[i])
            b += int(boxes[n-1-i])
            f_total += f
            b_total += b
        return answer
