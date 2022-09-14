class Solution:
    def findMinDifference(self, timePoints: List[str]) -> int:
        # HH:mm 형식을 분단위로 변환
        def convertToMinite(time):
            return (int(time[0:2]) * 60) + int(time[3:5])
        
        vals = []  # 분단위로 바꾼 값들
        for tp in timePoints:
            vals.append(convertToMinite(tp))
        vals.sort()
        # print(vals)
        minDiff = 1440 - vals[-1] + vals[0]  # 가장 마지막도 첫 값이랑 비교해주기 위해. 거꾸로 가는 diff를 계산
        for i in range(len(vals)):
            minDiff = min(minDiff, abs(vals[i] - vals[i-1]))
            
        return minDiff
