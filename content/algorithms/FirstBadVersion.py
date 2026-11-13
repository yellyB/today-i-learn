# The isBadVersion API is already defined for you.
# @param version, an integer
# @return an integer
# def isBadVersion(version):

class Solution:
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        left = 1
        right = n - 1
        while left <= right:
            mid = left + (right - left) // 2  # 앞에 left를 더하는건 그래야 절반의 절반 갈때 그 위치로 가기 가능
            if isBadVersion(mid):
                right = mid - 1  # 이보다 앞에 bad가 있을 수 있으니 ㄱㄱ
            else:
                left = mid + 1

        return left

    # binary Search 이용. 절반 확인해서 걔보다 큰지 작은지. 그래서 절반을 다시 갱신. 이걸 찾을때까지