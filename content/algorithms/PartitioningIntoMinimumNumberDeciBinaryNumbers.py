class Solution:
    def minPartitions(self, n: str) -> int:
        '''
        n중 가장 큰 숫자를 뽑으면
        그 숫자를 만들기 위해서 더해야 하는 횟수가 나오게 됨
        나머지 숫자는 신경 쓸 필요 없음
        '''
        return int(max(n))
