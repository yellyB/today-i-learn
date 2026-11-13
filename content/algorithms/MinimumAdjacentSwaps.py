class Solution:
    def getMinSwaps(self, num: str, k: int) -> int:
        numList = list(num)

        def getNextGreaterValue():
            # [i~끝]이 내림차순이면 그 범위는 더이상 스왑할 숫자가 없단 뜻
            # 그러면 [i-1]이 [i]보다 작다면 [i-1]이 [:i]중에서 가장 작은 숫자로 스왑되어야함
            # 그리고 그 뒤 숫자들은 오름차순 정렬되어야함
            i = len(num)-1
            while i > 0:
                if numList[i-1] < numList[i]:
                    # 이제 num[i-1]이랑 그 뒷 리스트 중 min값을 스왑해야하는데
                    # min값이 num[i-1]보다 커야지만 num보다 큰 숫자가 만들어짐
                    # 내림차순으로 되어있으니까 맨 뒤부터 확인해보면 됨
                    j = len(num)-1
                    while j > 0:
                        if numList[i-1] < numList[j]:
                            numList[i-1], numList[j] = numList[j], numList[i-1]
                            numList[:] = numList[:i]+sorted(numList[i:])
                            return
                        else:
                            j -= 1
                i -= 1

        def getAnswer():
            # 주어진num의 [i]가 바뀐리스트 몇번째에 있는지 확인함
            # 두 인덱스 차이가 스왑해야하는 횟수임(nunList[?]에서 num[i]까지 가려면 스왑해야하는 횟수니까)
            # print(num,numList)
            cnt = 0
            for i in range(len(num)):
                if num[i] != numList[i]:  # 서로 같은 위치의 데이터가 다르면 같은거 찾으러 ㄱㄱ
                    j = i+1
                    while j<len(numList):
                        if num[i] == numList[j]:
                            temp = numList.pop(j)
                            numList.insert(i,temp)
                            cnt = cnt+(j-i)
                            # print(numList, cnt)
                            break
                        j += 1
            return cnt


        while k > 0:
            getNextGreaterValue()  # k번 만큼 다음 큰 수 찾기를 실행함
            k = k - 1

        return getAnswer()