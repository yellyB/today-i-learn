class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda x:x[0])  # 1. [0]으로 정렬하고
        res = [intervals[0]]
        print(intervals)
        # 2. 기존 값의 마지막이랑 비교해서 연장을 할지 말지
        for i in range(1, len(intervals)):
            if res[-1][1] >= intervals[i][0]:
                if res[-1][1] >= intervals[i][1]: continue  # 연장이 소용없으면 패쓰
                res[-1][1] = intervals[i][1]
            else:
                res.append(intervals[i])
        
        return res
