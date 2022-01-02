class Solution:
    def findSubsequences(self, nums: List[int]) -> List[List[int]]:
        answer = []
        size = len(nums)

        def func(selected, nums):
            used = []  # 중복 방지
            if len(nums) == 0:
                return
            for i, n in enumerate(nums):
                if selected[-1] <= n and n not in used:
                    used.append(n)
                    if selected + [n] not in answer:
                        answer.append(selected + [n])  # 정답에 추가
                        func(selected + [n], nums[i + 1:])  # 선택목록에 추가하여 또 ㄱㄱ
            return

        for i in range(size - 1):  # 마지막은 최소2개 될 수 없으니 제외
            func([nums[i]], nums[i + 1:])
        return answer

    # https://leetcode.com/problems/letter-tile-possibilities/
    # 1079. Letter Tile Possibilities
    # 위 문제 응용함
