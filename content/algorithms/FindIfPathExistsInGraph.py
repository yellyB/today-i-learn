class Solution:
    def validPath(self, n: int, edges: List[List[int]], start: int, end: int) -> bool:
        if start == end: return True

        conn = [[] for i in range(n)]

        for edge in edges:
            conn[edge[0]].append(edge[1])
            conn[edge[1]].append(edge[0])

        def getConn(i):
            visited = []  # 방문한 이웃 노드 다시 안가기위해
            neighbors = conn[start]  # 여기에 저장된 이웃들을 하나씩 확인할거임
            visited.append(start)
            # print('neighbors:', neighbors)
            while len(neighbors) > 0:
                next = neighbors.pop(0)  # 먼저 들어온애부터꺼냄(LILO로하면 타임리밋)
                if next == end:
                    return True
                else:
                    if next not in visited:
                        neighbors.extend(conn[next])  # 이웃의 이웃도 확인 ㄱ
                        visited.append(next)

        # print('conn:', conn)

        return getConn(start)

    # 이중배열에 연결 정보를 다 저장  ex) 0번에 연결된게 1이랑 4면 [1,4]로
    # 그 데이터 차례로 꺼내면서 도착노드가 존재하는지 확인