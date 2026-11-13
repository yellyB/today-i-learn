class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        notIn = 0
        for word in words:
            for w in word:
                if w not in allowed:
                    notIn += 1
                    break

        return len(words)-notIn