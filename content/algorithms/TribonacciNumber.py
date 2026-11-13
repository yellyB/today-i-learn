class Solution:
    def tribonacci(self, n: int) -> int:
        memoization = [0] * (n+1)
        if len(memoization) > 1:
            memoization[1] = 1
        if len(memoization) > 2:
            memoization[2] = 1
        for i in range(3, n+1):
            memoization[i] = memoization[i-3] + memoization[i-2] + memoization[i-1]
        return memoization[n]