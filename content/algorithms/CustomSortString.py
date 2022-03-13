class Solution:
    def customSortString(self, order: str, s: str) -> str:
        ordered = []
        rest = []
        freq = {}
        
        for ss in s:
            if ss in freq: freq[ss] += 1
            else: freq[ss] = 1
                
        for o in order:
            idx = s.find(o)
            if idx > -1:
                ordered.extend([o] * freq[o])
                
        for ss in s:
            idx = order.find(ss)
            if idx == -1:
                rest.append(ss)
                
        print(ordered, rest)
        return ''.join(ordered+rest)
