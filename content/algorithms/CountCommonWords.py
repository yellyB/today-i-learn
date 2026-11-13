class Solution:
    def countWords(self, words1: List[str], words2: List[str]) -> int:
        freq1 = collections.defaultdict(int)
        freq2 = collections.defaultdict(int)

        for word in words1:
            freq1[word] += 1

        for word in words2:
            freq2[word] += 1

        cnt = 0
        for item in freq1.items():  # 첫 딕셔너리 돌려서
            if item[1] == 1 and freq2[item[0]] == 1:  # 값이 1인게 둘째 딕셔에서도 1이면 카운트 올림
                cnt += 1

        return cnt