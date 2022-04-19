class Solution:
    def minNumberOperations(self, target: List[int]) -> int:
        cnt = 1  # 타겟은 무조건 1이상이니까 0->1은 미리 계산
        prev = 1  # 위의 이유로 이전값은 1로 설정
        for t in target:
            if prev < t:
                cnt += t-prev
            prev = t
        return cnt
    
    """
    앞에꺼보다 크면 앞-지금 비교해서 그 차이만큼 더 변경시키면 되고
    앞보다 작으면 앞이랑 묶어서 증가할 수 있단거임.
    """
