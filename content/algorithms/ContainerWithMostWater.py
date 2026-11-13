class Solution:
    def maxArea(self, height: List[int]) -> int:
        # 물 양은 높이(두쪽중 작은 값) X 가로(인덱스의 차이) 하면 됨
        def calcWater(leftIdx, rightIdx):
            left, right = height[leftIdx], height[rightIdx]
            return min(left, right) * (rightIdx - leftIdx)

        leftIdx, rightIdx = 0, len(height) - 1  # 맨처음에 양 끝에서 시작
        water = 0

        while leftIdx < rightIdx:
            water = max(water, calcWater(leftIdx, rightIdx))
            # right값이 더 크다면 걘 그대로 놔두고 left가 움직여야 더 큰 값이 될거라고 예상되니까.
            if height[leftIdx] < height[rightIdx]:
                leftIdx += 1
            else:
                rightIdx -= 1

        return water