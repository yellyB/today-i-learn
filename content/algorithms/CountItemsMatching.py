class Solution:
    def countMatches(self, items: List[List[str]], ruleKey: str, ruleValue: str) -> int:
        keyIdx = {"type":0, "color":1, "name":2}
        j = keyIdx[ruleKey]
        cnt = 0
        for item in items:
            if item[j] == ruleValue:
                cnt += 1
        return cnt