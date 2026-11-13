class Solution:
    def scheduleCourse(self, courses: List[List[int]]) -> int:
        q = []
        days = 0
        
        courses.sort(key=lambda x:x[1])
        
        for course in courses:
            if days+course[0] <= course[1]:  # 총 걸린일수랑 이번에 걸리는 일 수 합친게 더 적어야
                days += course[0]
                heappush(q, -course[0])  # 큰 순으로 정렬되라고 음수로 저장
            
            elif q and -q[0] > course[0]:  # 저장된게 지금 걸리는거보다 더 오래걸리면 지금껄로 대체하기
                days += course[0] + heappop(q)
                heappush(q, -course[0])
                
        return len(q)
