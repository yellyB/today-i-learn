class Solution:
    def countGoodRectangles(self, rectangles: List[List[int]]) -> int:
        num = 0
        cnt = 0
        for l, w in rectangles:
            temp = min(l, w)
            if num == temp:
                cnt += 1
            elif num < temp:
                num = temp
                cnt = 1
        return cnt