class Solution:
    def numTimesAllBlue(self, light: List[int]) -> int:
        maxBulb = 0
        turnOn = 0
        moment = 0
        for l in light:
            maxBulb = max(maxBulb, l)
            turnOn += 1
            if maxBulb == turnOn:
                moment += 1
        return moment

# 맨 처음 켜진 전구가 3번이면 (3보다 작은) 전구 2개가 켜져야 파란색됨
# 그 말은 지금까지의 전구위치max만큼의 전구가(더 앞에만 셋을때)켜져야 된단뜻