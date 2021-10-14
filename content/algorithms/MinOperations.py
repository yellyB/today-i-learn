class Solution:
    def minOperations(self, nums: List[int]) -> int:
        cnt = 0
        beforeNum = 0
        for num in nums:
            if beforeNum >= num:  # 앞에숫자 저장한거랑 비교
                gap = beforeNum - num  # 앞 숫자와의 차이
                willPlus = gap + 1  # 높여줘야 하는 값
                cnt += willPlus  # 차이나는거 +1만큼 높여줘야함
                beforeNum = num + willPlus  # 높여준 값이 새로운 값이 됨
            else:
                beforeNum = num

        return cnt