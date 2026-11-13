class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rowLen = len(matrix)
        colLen = len(matrix[0])
        start, end = 0, (rowLen * colLen)
        while start < end:
            mid = (start + end) // 2  # 여기서 몫은 row고 나머지는 col위치임
            val = matrix[mid // colLen][mid % colLen]
            if val == target:
                return True
            elif val < target:
                start = mid + 1
            elif val > target:
                end = mid
        return False

