class Solution:
    def customSortString(self, order: str, s: str) -> str:
        ordered = []
        rest = []
        freq = {}
        
        # 중복 알파벳 추가 위해 빈도구함
        for ss in s:
            if ss in freq: freq[ss] += 1
            else: freq[ss] = 1
        
        # 먼저 order에 있는 문자가 s에 있는 경우부터 조사
        for o in order:
            idx = s.find(o)
            if idx > -1:
                ordered.extend([o] * freq[o])
        
        # order에는 없고 s에만 있는 문자 조사
        for ss in s:
            idx = order.find(ss)
            if idx == -1:
                rest.append(ss)
                
        return ''.join(ordered+rest)
