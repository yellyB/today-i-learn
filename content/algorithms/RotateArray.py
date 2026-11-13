class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        length = len(nums)

        if length < k:
            k = k % length

        cutIdx = length - k  # 잘라야 하는 기준 인덱스

        nums[:] = nums[cutIdx:] + nums[:cutIdx]

        # k번 만큼 맨뒤꺼를 맨 앞으로 옮기는건 만약 k가 3이라면 뒤에서 3개만큼을 앞으로 옮기면 됨
        # k가 len보다 클 때만 처리해주면 끝