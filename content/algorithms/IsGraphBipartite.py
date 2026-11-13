class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        '''
        문제 요약하자면 어떤 노드랑 연결된 모든 노드를 같은 색으로 칠했을 때
        최종적으로 각 노드들이 내 옆에있는 노드랑 같은 색이면 안됨
        ''' 
        
        A, B = set(), set()
        
        for u in range(len(graph)):
            if u not in A and u not in B:
                queue = [(u, A, B)]
                while queue:
                    u, a, b = queue.pop(0)
                    for v in graph[u]:
                        if v in a:
                            return False
                        elif v not in b:
                            b.add(v)
                            '''
                            지금, v가 b에 들어갔기때문에 내가 이번턴에 큐에 넣은 다른애를 체크할 때
                            v가 a에도 들어가게면 안됨(그렇게되면 A랑 B 둘 다에 포함되니까)
                            그래서 다음번 검사때 [1]번째 들어있으면 false를 리턴하도록 b,a로 순서 바꿔 넣음
                            Example 1을 예시로 들면,
                            첫 턴에 1,2,3이 한 묶음으로 묶이는데
                            그 다음번인 [0,2]를 검사할 때, 0까지는 1,2,3과 다른 묶음에 넣으면 되지만
                            2가 0과 같은 묶음에 들어가야 하는데 1,2,3묶음에 이미 있음
                            이러면 무슨 색을 배정해야 하는지 결정이 안되는거임
                            ''' 
                            queue.append((v, b, a))
                            
        return True
    
