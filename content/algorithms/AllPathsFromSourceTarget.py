class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        def getPath(curr, currPath):
            if curr == target:  # 목적지 도달했으면 정답에 추가 후 종료
                answer.append(currPath)
                return
            for i in graph[curr]:  # 후보 루트 탐색
                getPath(i, currPath + [i])
            return
        
        target = len(graph) - 1
        answer = []
        getPath(0, [0])  # 현위치, 현루트
        return answer
