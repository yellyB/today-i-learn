class Solution:
    def smallestEquivalentString(self, s1: str, s2: str, baseStr: str) -> str:
        UF = {}  # key: 노드, value: 대표
        def find(x):
            UF.setdefault(x,x)
            if x != UF[x]:  # 자기 자신이 대표 아니면?
                UF[x] = find(UF[x])  # 대표 찾기
            return UF[x]

        def union(x, y):
            rootX = find(x)
            rootY = find(y)
            UF[rootX] = UF[rootY] = min(rootX, rootY)


        for ss1, ss2 in zip(s1, s2):
            union(ss1, ss2)

        res = ''
        for s in baseStr:
            res += find(s)

        return res
