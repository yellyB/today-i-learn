class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        freq = collections.defaultdict(int)
        for a in arr:
            freq[a] += 1
        vals = freq.values()

        isIn = []
        for i in vals:
            if i in isIn:
                return False
            else:
                isIn.append(i)

        return True
