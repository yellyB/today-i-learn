class Solution:
    def equationsPossible(self, equations: List[str]) -> bool:
        UF = {}
        def find(x): # 대표 데려와
            UF.setdefault(x,x)
            if x != UF[x]: # x == UF[x] 조건을 만족한다는 말은, 이미 지가 대표란 것임 
                UF[x] = find(UF[x]) # 이건 위 만족하지 않을때이므로, 위에 누군가가 있단것임
            return UF[x]

        def union(x,y):
            rootX = find(x) # 니네 대표 데려와
            rootY = find(y) # 니네 대표도 데려와
            UF[rootX] = UF[rootY] = min(rootX, rootY) # 두 대표 중 더 쎈애로 교체!

        def parse(eq):
            left = eq[0]
            right = eq[3]
            sign = eq[1:3]
            return left, right, sign
        
        not_eqs = []  # 같지 않은애들은 따로 저장 후 나중에 비교
        for eq in equations:
            left, right, sign = parse(eq)
            if sign == '==':
                union(left, right)
            else:
                not_eqs.append((left, right))

        # 미리 저장해뒀던 == 였던 애들을 기준으로 검증.
        # not_eqs 에 저장했는데, 걔네가 같다고 나온다? 그럼 거짓
        for left, right in not_eqs:
            if find(left) == find(right):
                return False

        return True
