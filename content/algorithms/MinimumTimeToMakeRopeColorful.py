class Solution:
    def minCost(self, colors: str, neededTime: List[int]) -> int:
        ans = 0
        # greedy로, 바로 앞에꺼랑 비교해서 적은 코스트 풍선 없애기
        for i in range(1, len(colors)):
            if colors[i-1] == colors[i]:
                if neededTime[i-1] < neededTime[i]:
                    ans += neededTime[i-1]
                else:
                    ans += neededTime[i]
                    neededTime[i] = neededTime[i-1]
                    # △ 예외케이스 방어: 만약 똑같은 풍선 3개 5,4,8인 경우면
                    # 적은 코스트를 지우니까 4가 제일먼저 지워질텐데
                    # 그렇게하면 그 다음번 인덱스 검사할 때 또 4가 코스트 적기때문에
                    # 또 4에 해당하는 풍선 지우게됨
                    # 그래서 4자리에 그 다음으로 적은 코스트를 넣어주는것
        
        return ans