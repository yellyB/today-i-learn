class Solution:
    # 다음 key로 넘어가는 구간마다의 최소값을 구해서 각 ring 저장
    # (어디서 시작했는지에따라, 왼or오에 따라 달라지겠지?)
    # 알아야될 데이터 : 마지막 선택 위치, 그 위치까지 가는데 걸린 거리
    # [for 1] key 돌림
    # [for 2] 이 전에 key였던 ring에서의 위치 저장한 리스트 돌림
    # [for 3] ring돌림.  -> 여기서 왼쪽, 오른쪽 간 경우 비교해서 작은 값 저장
    def findRotateSteps(self, ring: str, key: str) -> int:
        lastIdxs = {0: 0}  # (마지막선택위치 : 걸린 거리) 초기값 지정 (여러개될수도있음)
        for k in key:
            temp = {}  # 선택한 알파벳 위치 저장하기 위한 임시변수
            for lastIdx in lastIdxs:
                for i, r in enumerate(ring):
                    if k == r:
                        minGap = min(abs(lastIdx - i), len(ring) - abs(lastIdx - i))  # 왼, 오 중에 더 작은 간격
                        if i not in temp:
                            temp[i] = minGap + lastIdxs[lastIdx]
                        else:
                            temp[i] = min(temp[i], minGap + lastIdxs[lastIdx])
            # 이번 for문에서 key에 해당했던 ring 위치를 last선택에 저장하고 다음for문으로
            lastIdxs = temp

        return min(lastIdxs.values()) + len(key)  # 버튼 누른 횟수 추가