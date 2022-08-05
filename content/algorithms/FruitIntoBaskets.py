class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        l = 0
        cnt = 0
        basket = defaultdict(int)  # 과일별 개수 저장
        
        for i, fruit in enumerate(fruits):
            basket[fruit] += 1  # 개수 증가시키고
            
            # 바구니에 3종류 이상이면
            while len(basket) >= 3:
                firstFruit = fruits[l]  # 제일 처음 담은 과일을
                basket[firstFruit] -= 1  # 빼줌
                if basket[firstFruit] == 0:  # 해당과일을 다 뺐다?
                    basket.pop(firstFruit)  # 빈 바구니 아예 제거
                l += 1  # 다음번엔 다음과일 검사하기 위해
            cnt = max(cnt, i-l+1)
        
        return cnt
