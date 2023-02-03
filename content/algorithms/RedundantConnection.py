class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        UF = list(range(len(edges)))
        def find(x): # 대표 데려와
            if x != UF[x]: # x == UF[x] 조건을 만족한다는 말은, 이미 지가 대표란 것임 
                UF[x] = find(UF[x]) # 이건 위 만족하지 않을때이므로, 위에 누군가가 있단것임
            return UF[x]

        def union(x, y):
            rootX = find(x) # 니네 대표 데려와
            rootY = find(y) # 니네 대표도 데려와
            UF[rootX] = rootY

        for i, j in edges:
            if find(i-1) == find(j-1):  # 과거에 똑같았던 적이 있었으면 그거 리턴
                return([i,j])
            else:
                union(i-1, j-1)
        
