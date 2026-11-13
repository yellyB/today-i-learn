class Solution:
    def stoneGame(self, piles: List[int]) -> bool:
        tempResult = {}
        def dpAlexTurn(i, j):
            if i > j:
                return 0
            if (i, j) in tempResult:
                return tempResult[(i, j)]
            # Alex의 선택 + Lee가 선택하고 남은 것 중 Alex의 선택
            tempResult[(i, j)] = max(piles[i] + dpLeeTurn(i + 1, j), piles[j] + dpLeeTurn(i, j - 1))
            return tempResult[(i, j)]

        def dpLeeTurn(i, j):
            if (i, j) in tempResult:
                return tempResult[(i, j)]
            tempResult[(i, j)] = min(dpAlexTurn(i + 1, j), dpAlexTurn(i, j - 1))
            return tempResult[(i, j)]

        alex = dpAlexTurn(0, len(piles) - 1)
        lee = sum(piles) - alex
        return alex > lee