class Solution:
    def canCross(self, stones: List[int]) -> bool:
        canJumpIdxs = {}  # n번째 돌에서 뛸 수 있는 인덱스들 저장
        target = stones[-1]

        if stones[1] != 1:
            return False

        for stone in stones:
            canJumpIdxs[stone] = []  # 일단 빈 값 넣어줌

        canJumpIdxs[0] = [1]  # 0에서 1갈때 1칸뛰는건 고정이니까

        for nowIdx in stones:  # 현재 돌 위치 = nowIdx
            if target in canJumpIdxs[nowIdx]:
                return True
            # ▽ 갈 수 있는 위치들 저장한것 차례로 꺼냄(거기로 갔다고 가정)
            for nextIdx in canJumpIdxs[nowIdx]:
                gap = nextIdx - nowIdx
                canJumpIdx = nextIdx + gap

                for jump in range(gap - 1, (gap + 1) + 1):
                    canJumpIdx = nextIdx + jump  # 여기서 갈 수 있는 인덱스
                    if nextIdx == canJumpIdx:  # 자기 자신으로 점프는 걍 패쓰
                        continue
                    # 이미 저장되지 않았고 / 가려는 곳이 물이 아닌 돌 이면(jumpIdxs에 있으면)
                    if canJumpIdx not in canJumpIdxs[nextIdx] and canJumpIdx in canJumpIdxs:
                        canJumpIdxs[nextIdx].append(canJumpIdx)

            # print(canJumpIdxs)
        return False

# <1 for문>
# stones for문돌림
# 그럼 stone(현재)에 해당하는 nexts(가능 점프위치)이 나오겠지? (딕셔너리 밸류값_

# <2 for문>
# 그것들을 또 돌려.
# 그럼 gap을 구할 수 있음. next(다음) - stone(현재)
# 지금 next로 뛰었다고 가정한거임.
# 그럼 gap은 이 전의 점프 칸이 되겠지?

# <3 for문>
# 그걸로 -1 ~ +1범위를 for문 돌림
# gaps[next]에 저장할건데
# 갈 수 있는 돌위치= stones에 있는지 확인
# 해서 [next]에다가 저장함

# <검사>
# 점프 가능 idx들 중에 stones의 마지막 인덱스 한 번이라도 포함되면 True
