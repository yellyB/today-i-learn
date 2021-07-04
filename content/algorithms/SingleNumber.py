class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        temp = []  # 요소를 저장, 같은 값의 요소가 있으면 제거할거임
        for num in nums:
            if num in temp:
                temp.remove(num)
            else:
                temp.append(num)

        return temp[0]