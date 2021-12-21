class Solution:
    def minFlips(self, target: str) -> int:
        flipCnt = 0
        restBulbsVal = '0'  # 반전시킨 뒤에 애들 현재 값
        for bulb in target:
            if bulb != restBulbsVal:
                flipCnt += 1
                restBulbsVal = '1' if restBulbsVal == '0' else '0'  # 값 반전
        return flipCnt