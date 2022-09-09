class Solution:
    def smallestRange(self, nums: List[List[int]]) -> List[int]:
        # 슬라이딩 윈도우
        num_idx = [[n, i] for i, num in enumerate(nums) for n in num]
        num_idx.sort(key=lambda x:x[0])
        
        res = []
        l = 0
        cnt = collections.defaultdict(int)  # 인덱스 별로 하나씩 숫자 알고있기 위해 카운트 이용할거임
        
        for r, item in enumerate(num_idx):
            cnt[item[1]] += 1
            while len(cnt) == len(nums):
                if not res or num_idx[r][0] - num_idx[l][0] < res[1] - res[0]:  # 저장된 차이보다 작다면 교체
                    res = [num_idx[l][0], num_idx[r][0]]
                    
                cnt[num_idx[l][1]] -= 1  # 슬라이딩 범위 첫 칸 이동하기 위해
                if cnt[num_idx[l][1]] == 0:
                    cnt.pop(num_idx[l][1])
                    
                l += 1
        
        return res
