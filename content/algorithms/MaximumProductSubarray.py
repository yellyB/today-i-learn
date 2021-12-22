class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        length = len(nums)
        idx0 = nums[0]

        totalMax = idx0
        maxVal = 1
        minVal = 1

        if idx0 > 0:
            maxVal = idx0
        elif idx0 < 0:
            minVal = idx0

        for num in nums[1:]:
            maxVal = num * maxVal  # 이전꺼의 maxVal이랑 계산
            minVal = num * minVal  # 이전꺼의 minVal이랑 계산

            maxVal, minVal = max(num, maxVal, minVal), min(num, maxVal, minVal)
            totalMax = max(totalMax, maxVal)

        return totalMax

    # 최종 max값(=totalMax)을 리턴할거임
    # 각 턴에서 이전 턴에서의 max값과 min값을 [i]값이랑 곱함
    # [i], [i]*max, [i]*min  이 세개중 max랑 min값을 구해서 각각 갱신해줌
    # -- 여기서 [i]값도 비교에 포함하는 이유:
    #    [i]를 subarray의 처음으로 계산할수도 있으니깐!
    # 방금 구한 max값은 totalMax에 갱신해주자

    # 설명 더 하자면:
    # 곱셈은 마이너스 부호 때문에 가장 작은값이 순식간에 가장 큰 값이 될 수가 있음
    # 그래서 max값이랑 min값을 각각 저장하고 있는거임