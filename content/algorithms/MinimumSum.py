class Solution:
    def minimumSum(self, oldNum: int) -> int:
        # 결과가 min이려면 일단 1. 두개로 쪼개서 더해야하고  2. 큰수 2개는 일의자리, 작은수 2개는 십의자리 와야함
        num = sorted(str(oldNum))
        
        front = int(num[0]) + int(num[1])
        back = int(num[2]) + int(num[3])
        
        q, r = divmod(back, 10)
        
        return (front + q)*10 + r
