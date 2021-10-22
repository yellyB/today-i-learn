class Solution:
    def shortestToChar(self, s: str, c: str) -> List[int]:
        p1 = s.index(c)  # 제일 먼저 만나는 c
        p2 = s[p1 + 1:].find(c) + p1 + 1  # 그 다음으로 만나는 c
        answer = []

        for i in range(len(s)):
            gap1 = abs(p1 - i)
            gap2 = abs(p2 - i)
            if gap1 > gap2:  # 그 다음 c위치가 더 가까워짐. 갱신해줘야함
                answer.append(gap2)
                p1 = p2
                p2 = s[p1 + 1:].find(c) + p1 + 1
            else:
                answer.append(gap1)

        return answer

    # p1에는 곧 만나는 c중 가장 가까운 위치, p2는 두번째로 가까운 c의 위치 저장
    # 문자열의 위치가 p1에서 가까운지 p2에서 가까운지 확인. 가까운애로 저장.
    # 문자열의 i가 p1보다 p2에 가까워졌다면 p2를 p1으로, p2는 다음번 c의 위치로