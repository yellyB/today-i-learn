class Solution:
    def decode(self, encoded: List[int], first: int) -> List[int]:
        answer = [first]
        for code in encoded:
            xor = code^first
            answer.append(xor)
            first = xor
        return answer