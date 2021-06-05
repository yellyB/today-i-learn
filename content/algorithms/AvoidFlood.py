class Solution:
    def avoidFlood(self, rains: List[int]) -> List[int]:
        result = []
        sunnyDays = []
        lakeNumLastRainDayPair = dict() #마지막으로 비가온 날 (호수번호/마지막비)
        for today in range(0, len(rains)):
            lakeNum = rains[today]
            #비x
            if lakeNum == 0:
                result.append(1)
                sunnyDays.append(today)
            #비o
            else:
                #비가 온적이 있는 호수인지?
                if lakeNum in lakeNumLastRainDayPair:
                    #비온적있음
                    lastRainDay = lakeNumLastRainDayPair[lakeNum] #마지막으로 비온날짜 가져옴
                    isAvoidable = False
                    for sunnyDay in sunnyDays:
                        if sunnyDay > lastRainDay: #마지마비온날짜보다 뒤에 맑은날있는지
                            isAvoidable = True
                            sunnyDays.remove(sunnyDay)
                            result[sunnyDay] = lakeNum
                            lakeNumLastRainDayPair[lakeNum]=today
                            break
                    if not isAvoidable:
                        return []
                else:
                    #비온적없음
                    lakeNumLastRainDayPair[lakeNum] = today #마지막으로 비온날짜 저장

                result.append(-1)
        return result