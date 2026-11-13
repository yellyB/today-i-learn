class Solution:
    def countGoodSubstrings(self, s: str) -> int:
        cnt = 0
        sets = collections.defaultdict(int)

        for i in range(len(s)):
            if i >= 3:
                k = s[i-3]
                sets[k] -= 1
                if sets[k] == 0:
                    del sets[k]

            if s[i] in sets:
                sets[s[i]] += 1
                continue
            else:
                sets[s[i]] += 1

            if len(sets) == 3:
                cnt += 1


        return cnt
