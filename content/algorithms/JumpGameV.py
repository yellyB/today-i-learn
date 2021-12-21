class Solution:
    def maxJumps(self, arr: List[int], d: int) -> int:
        jumpCnt = {}  # 각 막대기별 딴 막대기로 이동 할 수 있는 최대 숫자
        maxIdx = len(arr)

        def getMaxJumpCnt(idx):  # 인덱스 받아서 그 인덱스에서 최대 이동 할 수 있는 횟수 구하기
            if idx not in jumpCnt:
                jumpCnt[idx] = 0
            else:
                return jumpCnt[idx]

            now = arr[idx]  # 현재위치

            # 이동할 수 있는 범위 : (현재위치 - d) ~ (현재위치 + d) -> 현재위치는 제외

            # 왼쪽으로(현재위치 ~ 왼쪽으로 d칸까지)
            for moveIdx in range(idx - 1, max(0, idx - d) - 1, -1):
                if now <= arr[moveIdx]:  # 막히면 끝
                    break
                # 위에를 통과했다는건 이동이 가능하단뜻이니 +1해줌
                jumpCnt[idx] = max(jumpCnt[idx], getMaxJumpCnt(moveIdx) + 1)

            # 오른쪽으로
            for moveIdx in range(idx + 1, min(idx + d + 1, maxIdx)):
                if now <= arr[moveIdx]:
                    break
                jumpCnt[idx] = max(jumpCnt[idx], getMaxJumpCnt(moveIdx) + 1)

            return jumpCnt[idx]

        for i in range(len(arr)):
            getMaxJumpCnt(i)
        return max(jumpCnt.values()) + 1  # 맨 처음에 해당 위치에 디딘 횟수 더함