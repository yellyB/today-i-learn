class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        length = len(nums)
        isExist = [False] * (length + 1)  # 0값은 nums없지만 인덱스=숫자 를 맞추기 위해 한 칸 더 만듬
        answer = []
        for num in nums:
            isExist[num] = True

        for i in range(1, length + 1):
            if isExist[i] == False:
                answer.append(i)
        return answer