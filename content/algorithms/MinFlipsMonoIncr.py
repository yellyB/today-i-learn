class Solution:
    def minFlipsMonoIncr(self, s: str) -> int:
        # flip이 필요한 순간: 0나오다 1나오다 다시 0이 나오는 순간
        
        cnt_one = 0  # 1의 개수. 나중에 0을 만나면 0을 바꿀지 앞서만난 모든 1을 바꿀지 결정해야함
        cnt_flip = 0  # 1 뒤에 0이 나오면 얘넨 flip해야함. (0의개수 & 지금까지 flip한 횟수도 됨)
        
        for ss in s:
            if ss == '0': cnt_flip += 1
            else: cnt_one += 1
            
            # 이제까지 0만 나왔거나 / 0나온후 1만 이어지는 상황이면: 0으로 유지됨
            # 1이 더 많으면 이제껏 바꾼애들 유지하면 되고
            # 이제껏 flip횟수가 더 많으면 모든 1을 바꿔주는게 효율적
            cnt_flip = min(cnt_flip, cnt_one)
            
        return cnt_flip