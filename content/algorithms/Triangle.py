class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        for i in range(1, len(triangle)):
            maxColLen = len(triangle[i - 1]) - 1
            for j in range(len(triangle[i])):
                triangle[i][j] = min(triangle[i - 1][max(0, j - 1)], triangle[i - 1][min(maxColLen, j)]) + triangle[i][
                    j]
        return min(triangle[-1])

    # 931. Minimum Falling Path Sum 얘랑 똑같은 방법.
    # 윗 줄 j랑 j+1 확인해서 더 작은 값을 현재랑 더해서 갱신
    # 마지막줄 최소값 리턴