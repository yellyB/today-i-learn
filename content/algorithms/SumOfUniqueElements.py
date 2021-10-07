class Solution:
    def sumOfUnique(self, nums: List[int]) -> int:
        inNums = []  # 나왔던 숫자 저장
        notInNums = []
        for n in nums:
            if n not in notInNums:
                if n not in inNums:
                    notInNums.append(n)
            else:
                notInNums.remove(n)
                inNums.append(n)

        return sum(notInNums)