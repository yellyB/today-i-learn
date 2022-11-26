class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        # numerator 분자
        # denominator 분모
        quot = collections.defaultdict(dict)
        for (num, den), val in zip(equations, values):
            quot[num][num] = quot[den][den] = 1.0  # 자기 자신과의 연산은 1
            quot[num][den] = val  # 주어진 값을 기록
            quot[den][num] = 1 / val  # 주어진 값 이용해서 분모<->분자 인 값 계산
        
        # equations 에서 준 묶음 말고 다른 알파벳과의 계산값도 저장하기
        for k in quot:
            for i in quot[k]:
                for j in quot[k]:
                    # [i][j]를 할 때, 중간역할 해주는 애 덕분에 연결될 수 있음
                    # 예를들면,  ex1 의 경우에 k=b이면 b:{b,a,c}이기 때문에
                    # i랑 j가 a,c로 한번씩 되기 때문에, a랑 c가 서로한테 저장 될 수 있다.
                    quot[i][j] = quot[i][k] * quot[k][j]
        
        return [quot[num].get(den, -1.0) for num, den in queries]  # 없으면 -1.0로
