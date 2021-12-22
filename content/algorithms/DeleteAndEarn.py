class Solution:
    def deleteAndEarn(self, nums: List[int]) -> int:
        numsSum = [0] * (max(nums) + 1)
        for num in nums:
            pass
            numsSum[num] += num
        print(numsSum)

        def getMax(nums):
            if len(nums) < 2:
                return max(nums)
            vals = nums[:2]
            for i in range(2, len(nums)):
                # 누적값인 vals[i-1]에는 어떤 경로를 타고 왔든,
                # [i-1]에 도달할때까지 최고값이 저장되어 있음
                # 그 값이랑 주어진리스트인 nums[i-2]에 현재값을 더한거랑 비교
                vals.append(max(vals[i - 2] + nums[i], vals[i - 1]))
            return max(vals)

        return getMax(numsSum)

    # 문제 : 숫자n을 선택하면 n만큼 점수에 추가되고 n은 리스트에서 사라짐.
    #        그리고 n-1 과 n+1이 전부 사라짐. 이때 니가 얻을 수 있는 최고 점수 구하라
    # 방법 : 한 숫자를 선택하면 그 숫가자 몇개든 결국 전부 내 점수가 됨
    #        숫자의 개수만큼 곱하기를 해서 (예를들면 3이 2개다? 그럼 3:6점) 형태로 만든다
    #        만약 nums=[2,3]이면 [0,0,2,3]이 됨
    #        3을 선택하면 2랑 4의 값은 0으로 만들어버림
    #        값이 남아있는게 있을때까지 반복