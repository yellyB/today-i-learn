# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def nextLargerNodes(self, head: Optional[ListNode]) -> List[int]:
        values = []
        while head:
            values.append(head.val)
            head = head.next

        res = [0] * len(values)
        stack = []
        for i, val in enumerate(values):
            while stack and stack[-1][1] < val:
                s_idx, s_val = stack.pop()
                res[s_idx] = val
            else:
                stack.append((i, val))

        return res
