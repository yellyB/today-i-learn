class Solution:
    def deckRevealedIncreasing(self, deck: List[int]) -> List[int]:
        # 첨에 answer를 전부 0(=빈칸)으로 넣음
        # 빈 칸을(숫자 채워졌으면 그 칸은 pass)
        # 한 칸씩 건너뛰며 작은 숫자부터 채우기
        length = len(deck)
        answer = [0] * length

        deck.sort(reverse=True)

        i = 0
        isPassOnce = True  # 빈 칸 한 번 건너뛰었는지 체크하는 용도
        while len(deck) > 0:
            if answer[i] == 0:
                if isPassOnce == True:
                    answer[i] = deck.pop()
                    isPassOnce = False
                else:
                    isPassOnce = True

            i += 1
            if i > length - 1:
                i = length - i
        print(answer)
        return answer