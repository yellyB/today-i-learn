class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        maxSum = 0
        for i in range(0, len(accounts)):
            if maxSum < sum(accounts[i]):
                maxSum = sum(accounts[i])
        return maxSum
