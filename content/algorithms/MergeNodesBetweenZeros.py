# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        temp = head
        temp = temp.next
        curr = head
        sums = 0
        while temp:
            if temp.val:
                sums += temp.val
            else:
                curr = curr.next
                curr.val = sums
                sums = 0
            temp = temp.next
        curr.next = None
        return head.next
