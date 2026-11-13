class Solution:
    def numTilePossibilities(self, tiles: str) -> int:
        answer = set()

        def func(tile, restTiles):
            if tile:
                answer.add(tile)
            for i in range(len(restTiles)):
                func(tile + restTiles[i], restTiles[:i] + restTiles[i + 1:])
            return

        func('', tiles)
        return len(answer)

    # 답 보고 품 - 나중에 잊어먹고나서 다시 풀어보기
    # 타일스에서 한개씩 늘려가며 set에 넣을건디
    # 현재꺼+나머지tiles에서 한개씩추가한거   해서 set에 넣기
    # 개천재인듯..