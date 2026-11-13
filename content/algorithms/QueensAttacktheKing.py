class Solution:
    def queensAttacktheKing(self, queens: List[List[int]], king: List[int]) -> List[List[int]]:
        res = []
        def bfs(king, dx, dy):
            if 0<=king[0]<8 and 0<=king[1]<8:
                if king in queens:
                    res.append(king)
                else:
                    bfs([king[0]+dx,king[1]+dy], dx, dy)
        
        # 위부터 시계방향으로 검사
        bfs(king[:], -1, 0)
        bfs(king[:], -1, 1)
        bfs(king[:], 0, 1)
        bfs(king[:], 1, 1)
        bfs(king[:], 1, 0)
        bfs(king[:], 1, -1)
        bfs(king[:], 0, -1)
        bfs(king[:], -1, -1)
        
        return res
