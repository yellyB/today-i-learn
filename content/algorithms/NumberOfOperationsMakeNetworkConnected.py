class Solution:
    def makeConnected(self, n: int, connections: List[List[int]]) -> int:
        def dfs(i):
            if seen[i]:
                return 0  # 이미 연결 확인했으면 0개로 리턴

            seen[i] = 1  # 확인 표시. 모든 컴터가 딱 한번씩만 방문 체크되도록
            for j in link[i]:
                dfs(j)

            return 1


        if len(connections) < n-1:
            return -1

        # link = [set()] * n  -> 이거 안되네 ㅠㅠ
        link = [set() for i in range(n)]
        for conn in connections:
            link[conn[0]].add(conn[1])
            link[conn[1]].add(conn[0])
            

        seen = [0] * n
        res = 0
        for i in range(n):
            res += dfs(i)
        
        return res - 1
