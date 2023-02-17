# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        vals = []
        while head:
            vals.append(head.val)
            head = head.next
        
        n = len(vals)
        maxVal = 0
        for i in range(n//2):
            maxVal = max(maxVal, vals[i]+vals[n-i-1])
        return maxVal
