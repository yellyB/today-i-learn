class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        highest=0
        now=0
        for g in gain:
            now += g
            highest = max(highest, now)
        return highest