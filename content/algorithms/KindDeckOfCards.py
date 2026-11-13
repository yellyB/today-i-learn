class Solution:
    def hasGroupsSizeX(self, deck: List[int]) -> bool:
        if len(deck) == 1: return False
        groups = {}  # 카드숫자 : 몇개인지
        for card in deck:
            if card in groups:  # 있으면 갯수 + 1
                groups[card] += 1
            else:  # 없으면 갯수 = 1
                groups[card] = 1

        cntList = list(groups.values())
        cntList.sort()
        cnt2 = 0
        cnt3 = 0
        cnt5 = 0
        cnt7 = 0
        for cnt in cntList:
            if cnt % 2 == 0:
                cnt2 += 1
            if cnt % 3 == 0:
                cnt3 += 1
            if cnt % 5 == 0:
                cnt5 += 1
            if cnt % 7 == 0:
                cnt7 += 1

        if cnt2 == len(cntList) or cnt3 == len(cntList) or cnt5 == len(cntList) or cnt7 == len(cntList):
            return True
        else:
            return False