class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        costOfDays = {0:0}  # 날짜:가격
        lastDay = days[len(days)-1]  # 여행할 제일 마지막 날짜
        for day in range(1, lastDay+1):
            if day in days:  # 여행하려는 날짜에 있는지?
                dayAgo = day - 1
                weeksAgo = day - 7 if day - 7 >= 0 else 0
                monthAgo = day - 30 if day - 30 >= 0 else 0
                costOfDays[day] = costOfDays[dayAgo] + costs[0]  # 전날 가격에 1일권 가격 더함
                costOfDays[day] = min(costOfDays[day], costOfDays[weeksAgo] + costs[1])  # 7일전에 7일권을 샀을때와 가격비교
                costOfDays[day] = min(costOfDays[day], costOfDays[monthAgo] + costs[2])  # 30일전에 30일권 샀을때와 가격비교
            else:
                costOfDays[day] = costOfDays[day-1]
        return costOfDays[lastDay]