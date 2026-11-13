class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        freq = collections.defaultdict(int)
        for word in sorted(words):
            freq[word] += 1

        return sorted(freq, key=lambda x: freq[x], reverse=True)[:k]