class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        cars = []
        cnt = len(position)
        for p, s in zip(position, speed):
            cars.append([p,s])
            
        cars.sort(key=lambda x:x[0], reverse=True)  # 도착지에 가까운 순서대로
        prev = 0
        for car in cars:
            time = (target-car[0])/car[1]  # 도착지까지 걸리는 시간
            # print(time, prev)
            if prev >= time:  # 현재 차가 앞차보다 빨리 도착하면 연결가능
                cnt -= 1
            else:
                minSpeed = time
                prev = time  # 앞차에 연결 실패했으면 값 갱신. 연결성공하면 앞 스피드가 더 느린거니까 갱신필요없음
            
        return cnt
