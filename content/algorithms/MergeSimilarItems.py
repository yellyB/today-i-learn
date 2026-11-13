class Solution:
    def mergeSimilarItems(self, items1: List[List[int]], items2: List[List[int]]) -> List[List[int]]:
        sums = collections.defaultdict(int)
        for item in items1:
            sums[item[0]] += item[1]
        for item in items2:
            sums[item[0]] += item[1]

        sortedList = sorted(sums.items(), key=lambda x:x[0])
        res = []
        for item in sortedList:
            res.append(list(item))

        return res
