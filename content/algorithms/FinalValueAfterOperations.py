class Solution:
    def finalValueAfterOperations(self, operations: List[str]) -> int:
        answer = 0
        for op in operations:
            if '+' in op:
                answer += 1
            else:
                answer -= 1
        return answer