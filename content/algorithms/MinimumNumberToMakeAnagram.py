class Solution:
    def minSteps(self, s: str, t: str) -> int:
        freqT = [0] * 26
        freqS = [0] * 26
        for i in range(len(t)):
            freqT[97 - ord(t[i])] += 1
            freqS[97 - ord(s[i])] += 1

        cnt = 0
        for i in range(26):
            cnt += abs(freqT[i] - freqS[i])

        return cnt // 2  # 차이나는 알파벳을 제거하는것과 추가하는 카운트가 같이 세어졌으니까 반으로 나눔

    # 알파벳 개수인 26만큼 0으로 초기화 한 리스트.
    # 거따가 알파벳 빈도수 저장
    # 그래서 걍 비교