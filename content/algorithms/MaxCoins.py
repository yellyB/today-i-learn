class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        res = 0
        piles.sort(reverse=True)
        bob = len(piles)//3  # 밥이 선택하는 개수
        for i in range(1, len(piles)-bob, 2):
            res += piles[i]
        return res
    
    '''
    각각 선택하는 개수 = len/3
    
    세번째 순서인 밥은 제일 작은 숫자들만 선택하게 될거임
        => 내림차순 정렬하고 뒤에서 n/3개만큼 빼준상태로 시작
    
    그리고 첫번째는 앨리스니까 나는 두번째로 큰 수를 계속 선택하면 됨    
    '''
