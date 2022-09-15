class Solution:
    def findRelativeRanks(self, score: List[int]) -> List[str]:
        res = score[:]
        medal = ["Gold Medal","Silver Medal","Bronze Medal"]
        for i, s in enumerate(sorted(score, reverse=True)):
            if i < 3:
                res[res.index(s)] = medal[i]
            else:
                res[res.index(s)] = str(i+1)
        return res
