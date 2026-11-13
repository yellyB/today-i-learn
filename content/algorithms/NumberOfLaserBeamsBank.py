class Solution:
    def numberOfBeams(self, bank: List[str]) -> int:
        def count(strs):
            cnt = 0
            for s in strs:
                if s == '1':
                    cnt += 1
            return cnt
        
        ans = 0
        cnt = 0
        for b in bank:
            lCnt = count(b)  # 레이저 개수
            if lCnt == 0:  # 레이저 0개면 전전이랑 비교해야함. 걍 건너뛰기
                continue
            else:
                ans += (cnt * lCnt)  # 지난 레이저개수 x 이번 레이저개수 => 정답에 추가
                cnt = lCnt  # 이번 레이저는 지난 레이저로 미뤄줌
                
        return ans
