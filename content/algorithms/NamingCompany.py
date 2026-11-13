class Solution:
    def distinctNames(self, ideas: List[str]) -> int:
        # 1. 각각 prefix랑 나머지를 딕셔너리로 저장
        pairs = {}
        for idea in ideas:
            prefix = idea[0]
            if prefix in pairs:
                pairs[prefix].add(idea[1:])
            else:
                pairs[prefix] = set([idea[1:]])
        # print(pairs)

        # 2. 딕셔너리를 1번-2번 1번-3번. 2번-3번 ... 같이 짝지어서 개수 구하기
        cnt = 0
        keys = list(pairs.keys())
        n = len(keys)
        for i in range(n):
            for j in range(i+1, n):
                # [i]랑 [j]에서 공통되는 idea[1:]부분이 있다면 걔네는 이미 ideas에 있는 애들이라 계산에 포함되면 안된다.
                # 그래서 합집합의 개수를 구한다음 cnt를 계산할 때 빼주고 계산
                common = len(pairs[keys[i]].intersection(pairs[keys[j]]))
                cnt += (len(pairs[keys[i]])-common) * (len(pairs[keys[j]])-common) * 2
        
        return cnt
