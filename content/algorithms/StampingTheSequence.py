class Solution:
    def movesToStamp(self, stamp: str, targetStr: str) -> List[int]:
        res = []
        n = len(stamp)
        target = list(targetStr)
        tried = 0
        
        def find(word):
            startIdx = -1
            try:
                startIdx = ''.join(target).index(word)
            except:
                startIdx = -1
            return startIdx
        
        
        # 앞 혹은 뒤에서 하나씩 마킹한 문자열 각각 만들어서
        # 그걸 타겟에서 위치 찾음. 더이상 없을때까지.
        # 찾으면 ?로 마킹
        def marking(markCnt):
            mark = ('?'*(markCnt))
            
            # 앞부분 마킹
            fMark = mark + stamp[markCnt:]
            fRes = find(fMark)
            while fRes != -1:
                res.append(fRes)
                target[fRes:fRes+n] = ['?']*n
                fRes = find(fMark)
                
            # 뒷부분 마킹
            bMark = stamp[:n-markCnt] + mark
            bRes = find(bMark)
            while bRes != -1:
                res.append(bRes)
                target[bRes:bRes+n] = ['?']*n
                bRes = find(bMark)
            return
        
        # 한글자씩 ? 로 마킹해나가기
        for i in range(n):
            marking(i)
        
        if ''.join(target) == '?'*len(targetStr):
            return res[::-1]
        else:
            return []
