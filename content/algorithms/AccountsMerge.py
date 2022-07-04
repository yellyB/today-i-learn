class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        
        def dfs(idx):
            if visited[idx]:
                return
            emails = accounts[idx][1:]
            visited[idx] = True
            for acc in accounts[idx][1:]:
                for v in emailIdx[acc]:
                    res = dfs(v)
                    if res:
                        emails.extend(res)
            return emails
        
        
        
        # 1. 어느 이메일이 몇번째에 있는지 기록
        emailIdx = {}
        visited = [False] * len(accounts)
        
        for i, account in enumerate(accounts):
            for a in account[1:]:
                if a in emailIdx:
                    emailIdx[a].append(i)
                else:
                    emailIdx[a] = [i]
        
        answer = []
        
        
        # 2. 계정 돌면서 거기에 연결된 모든 계정을 emails에 묶을 것임
        for i in range(len(accounts)):
            if visited[i]:
                continue
            res = dfs(i)
            if res:
                answer.append([accounts[i][0]] + sorted(list(set(res))))
        
        
        return answer
