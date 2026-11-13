class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        # 그룹은 1씩 차이
        
        nums = collections.defaultdict(int)
        for h in sorted(hand): nums[h] += 1
            
        for [k, v] in nums.items():
            if v > 0:  # hand 에 있었거나 남은 개수 있단 뜻
                for i in range(1, groupSize):
                    if nums[k+i] <= 0:  # 1큰 다음 카드가 없으면 그룹 불가
                        return False
                    nums[k+i] -= 1  # 그룹에 사용한건 제외
        
        return True
