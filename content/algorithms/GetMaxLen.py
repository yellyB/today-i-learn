class Solution:
    def getMaxLen(self, nums: List[int]) -> int:
        plus = 0
        minus = 0
        for i, num in enumerate(nums):
            if num == 0:
                plus = 0
                minus = 0
                nums[i] = plus
            elif num > 0:
                plus += 1
                minus += 1 if minus > 0 else 0
                nums[i] = plus
            elif num < 0:
                plus, minus = minus, plus
                plus += 1 if plus > 0 else 0
                minus += 1
                nums[i] = plus
        return max(nums)

    # 152. Maximum Product Subarray 참고 (누적곱셈으로 가장 큰 값을 찾는거)
    # 이 문제는 누적 곱셈을 했을 때 양수가 나오는 가장 많은 부분배열 요소 갯수
    # plus개수와 minus개수를 갖고 있자
    # num이 마이너스면 plus였던 애들이 minus로 바뀌고 minus는 plus로 바뀜
    # 현재꺼까지 +1 해서 마이너스인 num의 이전이 p=2 m=1이었으면 마이너스를 만남으로서 p=2 m=3이 됨
    # 예외인 경우는 아직 plus개수가 0이거나 minus개수가 0인 경우다.
    # 만약 nums= [-1, 1]이라면 맨 처음 -1을 만났을 때
    # 어차피 반전될 마이너스 값이 없기때문에 plus에 그냥 0으로 넣는다. (반대도 마찬가지)
