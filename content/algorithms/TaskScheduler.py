class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        maxCharCnt = 0
        maxChar = tasks[0]
        charDict = {}
        
        for char in tasks:
            if char in charDict:
                charDict[char] += 1
            else:
                charDict[char] = 1
            
            if charDict[char] > maxCharCnt:
                maxCharCnt = charDict[char]
                maxChar = char
        
        idleCnt = (maxCharCnt - 1) * n  # 빈 칸 만들어준 셈
        
        for (char, cnt) in charDict.items():
            if char == maxChar: continue  # 건뛰
            if cnt == maxCharCnt:  # 최고개수 같은애가 있다면 최고개수문자열 바로옆에 놔주면 됨(idleCnt구할때랑 동일)
                idleCnt -= (cnt-1)
            else:  # 위에 두 경우 다 아니면 걍 개수만큼 자리 차지
                idleCnt -= cnt
        
        if idleCnt <= 0:
            return len(tasks)
        
        return len(tasks) + idleCnt
        
