class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        lastIdx = {}
        for i in range(len(s)):
            lastIdx[s[i]] = i

        slices = []
        tempMax = 0  # lastIdx[s[0]]  # 더 큰 idx가 나오기 전까지 임시 저장
        start, end = 0, 0

        # 현위치보다 마지막 등장 위치가 크면 적어도 거까진 가야해
        for i in range(len(s)):
            alpha = s[i]
            lastAppearIdx = lastIdx[alpha]
            if i <= lastAppearIdx:
                tempMax = max(tempMax, lastAppearIdx)
                if tempMax == i:  # 임시저장했던 최고idx랑 현위치 같으면 자를수있음
                    slices.append(i + 1 - start)  # 알파벳 몇개 들어가나
                    start = i + 1  # 다음 조각의 시작위치 갱신

        return slices

        # ex1에서 첫번째인 a를 자르려면 적어도 9번까지는 잘라야함
        # 0~9 사이의 알파벳이 나머지 파트에 없으니 얜 통과

        # 그 다음 10번째인 d는 적어도 defegd까지는 잘라야함
        # 근데 11번째인 e가 그 다음에도 나오네?
        # 그러면 하나 더 포함해서 defegde까지 잘라.
        # [12]인 f는 나머지 파트에 없으니 패스, 그 뒤로계속 마찬가지

        # 그럼 여기서 어떤 알파벳을 자르려면 얘가 그 뒤엣부분에 나오는지 알아야한단걸 알수있음
        # 그 말은 적어도 얘가 마지막으로 나오는 위치까지는 잘라야한단거
