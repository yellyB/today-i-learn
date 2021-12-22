class Solution:
    def trap(self, height: List[int]) -> int:
        if len(height) <= 2: return 0

        filled = 0
        left = 1
        right = len(height) - 2
        leftMax = height[0]
        rightMax = height[-1]

        while left <= right:
            if leftMax <= rightMax:
                leftH = height[left]
                if leftH >= leftMax:  # 채우려는 곳이 leftMax와 같,크면 채우지 못함
                    leftMax = leftH
                else:
                    # 왼 채우기
                    filled += leftMax - leftH
                left += 1
            else:
                rightH = height[right]
                if rightH >= rightMax:
                    rightMax = rightH
                else:
                    # 오 채우기
                    filled += rightMax - height[right]
                right -= 1

        return filled

# 물이 담기려면 양쪽이 컵 모양처럼 되어있어야.
# 만약 왼쪽부터 시작해서 i의 바로 오른쪽에 물을 채운다면
# 오른쪽이 왼쪽보다 같.크면 왼쪽 높이만큼 물을 채울 수 있음
# 그러니까 검사하고 있는 방향의 제일 끝이 현재보다 높다면 현재 높이만큼 물을 채울 수 있는 것
# 근데 검사하려는 방향의 제일 끝이 현재보다 낮다면?
# 그럼 반대로 거기서 여기까지 오면서 물을 채우면 됨
# 오른쪽부터 시작하면 현재보다 왼쪽이 높을 때 현재(오른쪽)만큼 채울 수 있기때문

