class Solution:
    def removeStones(self, stones: List[List[int]]) -> int:
        def dfs(idx, cnts):
            checked[idx] = True
            for i in range(n):
                if checked[i]: continue
                if stones[i][0] == stones[idx][0] or stones[i][1] == stones[idx][1]:
                    cnts = dfs(i, cnts+1)
            return cnts

        cnt = 0
        n = len(stones)
        checked = [False] * n
        for i in range(n):
            if not checked[i]:
                res = dfs(i, 0)
                cnt += res

        return cnt
