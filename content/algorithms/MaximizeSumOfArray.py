class Solution:
    def largestSumAfterKNegations(self, nums: List[int], k: int) -> int:
        # 음수 파트, 양수 파트 나눠서 진행할거임
        # 음수파트 : 음수 -> 양수
        # 양수파트 : 양수로 다 바꿨으면 다시 정렬해서 젤 작은 숫자만 음수로
        nums.sort()  # 처음 정렬
        i = 0
        while k > 0 and i < len(nums):
            if nums[i] > 0:  # 음수 파트 끝나면 종료
                break
            nums[i] += nums[i] * -2  # 양수로 변환
            k -= 1
            i += 1

        nums.sort()
        i = 0
        # 이 루프는 계속 인덱스 0만 바꿀
        while k > 0:
            nums[i] -= nums[i] * 2  # 음수로 변환
            k -= 1

        return sum(nums)