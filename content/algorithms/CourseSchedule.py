class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # cycle이 있으면 무조건 F이다.
        # cycle이 하나라도 있는지 확인해야함
        
        
        def dfs(key, visited):
            if key in visited: return False  # 확인중인 목록에 있으면 cycle일수밖에
            if key in checked: return True  # 완전 확인끝난 애들에 포함되어있다면 얜 안전. 확인할필요 X
            
            if key in pre:
                for val in pre[key]:
                    if not dfs(val, visited+[key]): return False
                    
            checked.append(key)  # 위 for문에서 중단당하지 않았다면 얜 안전!
            return True
        
        
        pre = {}  # 딕셔너리로 짝지을거. key를 얻으려면 [val]에 있는애들 먼저해야함
        checked = []  # 전부 다 봐서 cycle없는거 확인 끝마친 애들
        
        for p in prerequisites:
            if p[0] in pre: pre[p[0]].append(p[1])
            else: pre[p[0]] = [p[1]]
                
        
        # numCourses-1 까지 전부 통과해야 최종적으로 T를 리턴할 수 있음. 그러니 하나씩 다 검사
        for i in range(numCourses):
            if not dfs(i, []): return False  # 하나라도 F면 즉시 리턴
        
        return True
