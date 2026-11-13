class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        pair = []
        for name, height in zip(names, heights):
            pair.append([name, height])

        pair.sort(key=lambda x:x[1], reverse=True)

        res = []
        for val in pair:
            res.append(val[0])

        return res
