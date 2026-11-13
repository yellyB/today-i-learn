class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        sStack = []
        tStack = []
        for ss in s:
            if ss == '#' and sStack:
                sStack.pop()
            elif ss != '#':
                sStack.append(ss)
        for tt in t:
            if tt == '#' and tStack:
                tStack.pop()
            elif tt != '#':
                tStack.append(tt)
        
        
        return sStack == tStack
