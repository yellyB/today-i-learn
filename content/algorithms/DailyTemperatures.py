class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        # 오늘 온도가 어제보다 크면 저장 안할거니까
        # 여러개 저장되었다는건 시간지날수록 온도 낮아진다는 뜻
        # 오늘온도보다 작은 날까지만 거슬러 올라가면 됨. 거기부터 다시 저장 시작
        daysTemp = [[0, temperatures[0]]]
        answer = [0]*len(temperatures)
        for i in range(1, len(temperatures)):
            # print(daysTemp, i)
            while daysTemp and temperatures[i] > daysTemp[-1][1]:
                lastTemp = daysTemp.pop()
                answer[lastTemp[0]] = i - lastTemp[0]
            daysTemp.append([i, temperatures[i]])
        return answer